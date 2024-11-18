# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    access view

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/23 10:42"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:
    JWT = Json Web Token

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python access.py
# ------------------------------------------------------------
from datetime import timedelta, datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, status as http_status, Depends, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt, jws
from pydantic import BaseModel

from deploy.reqbody.access import TokenBody as Token, LoginBody
from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code
from deploy.utils.utils import d2s
from deploy.utils.exception import JwtCredentialsException
from deploy.config import JWT_TOKEN_SECRET_KEY, JWT_TOKEN_ALGORITHM, JWT_TOKEN_EXPIRE_MINUTES


# define view
access = APIRouter(prefix="/access", tags=["系统登陆与登出，使用JWT验证"])

TOKEN_DEFAULT_EXPIRE_MINUTES = 60 * 4  # 访问令牌过期时间，单位：分


"""
from表单：token
请求体：token_request_body
"""
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/access/token_request_body")

credentials_exception = HTTPException(
    http_status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@access.post("/token",
             response_model=Token,
             summary="用户Token API[OAuth2PasswordRequestForm]",
             description="依据用户[Form表单]提供的username，password参数（KEY不可更改），获取用户登录Token"
             )
async def access_token(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)) -> dict:
    """
    用户Token API
    :param form_data: Form表单对象
    :return: dict
    """
    username = getattr(form_data, "username", None)
    password = getattr(form_data, "password", None)
    if not username or not password:
        return Status(
            Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value,
            Status_enum.FAILURE.value,
            Status_msg.get(204),
            {}
        ).status_body

    # TODO 用户信息核对
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return {"access_token": token, "token_type": "Bearer"}


@access.post("/token_request_body",
             response_model=Token,
             summary="用户Token API[Request Body]",
             description="依据用户[Request Body]提供的username，password参数（KEY不可更改），获取用户登录Token"
             )
async def access_token_request_body(form_data: LoginBody) -> dict:
    """
    用户Token API
    :param form_data: Form表单对象
    :return: dict
    """
    username = getattr(form_data, "username", None)
    password = getattr(form_data, "password", None)
    # 缺少登录参数
    if not username or not password:
        return Status(
            Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value,
            Status_enum.FAILURE.value,
            Status_msg.get(204),
            {}
        ).status_body

    # TODO 用户信息核对
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return {"access_token": token, "token_type": "Bearer"}


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    generate access token
    :param data: [dict]数据
    :param expires_delta: [timedelta]过期时长
    :return: str

    要点：用utc时间类型
    """
    to_encode_data = data.copy()
    # token申请时间
    token_apply_time = data.get('apply_time') if data.get('apply_time') else datetime.utcnow()
    to_encode_data['apply_time'] = d2s(token_apply_time, fmt="%Y-%m-%d %H:%M:%S")
    # token过期日期
    expire = token_apply_time + expires_delta if expires_delta \
        else token_apply_time + timedelta(minutes=TOKEN_DEFAULT_EXPIRE_MINUTES)  # 如果没有配置默认登录时长，默认4h
    to_encode_data['expire_time'] = d2s(expire, fmt="%Y-%m-%d %H:%M:%S")
    to_encode_data.update({"exp": expire})  # jwt过期时间KEY：['exp', 'iat', 'nbf']
    encoded_jwt = jwt.encode(claims=to_encode_data, key=JWT_TOKEN_SECRET_KEY, algorithm=JWT_TOKEN_ALGORITHM)
    """jwt.encode
    参数解析：
        claims (dict): 存储Token数据
        key (str or dict): Token加码密钥（自定义）
        algorithm (str, optional): 算法（源码是使用hashlib加密）
    ----------------------------------------------------------------------
    返回值：
        str：加密形成的Token字符串
    """
    return encoded_jwt


async def decode_token_rtx(
        token: str = Depends(oauth2_schema)
):
    """
    Token解码用户的rtx-id
    :param token: [str]Token
    # :param only: [bool]True返回Token data数据的rtx_id，False返回Token data对象
    :return: [dict]Token data
    """
    try:
        claims = jwt.decode(token=token, key=JWT_TOKEN_SECRET_KEY, algorithms=[JWT_TOKEN_ALGORITHM])
        """jwt.decode
        参数解析：
            token (str): Token字符串
            key (str or dict): 定义Token时的密钥
            algorithms (str or list): 定义Token时的算法
        ----------------------------------------------------------------------
        返回值：
            dict: 解码加密后Token的data数据
        """
        rtx_id = claims.get("rtx_id")
        if rtx_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return rtx_id


async def verify_token_rtx(
        token: str = Depends(oauth2_schema),
        x_rtx_id: str = Header(..., min_length=1, max_length=25, convert_underscores=True, description="X-Rtx-Id")
):
    """
    校验Token解码后的rtx-id与用户Header传入的rtx-id是否一样
    :param token: [str]Token
    :param x_rtx_id: [str]用户X-Rtx-Id
    :return: [dict]Token data
    """

    try:
        claims = jwt.decode(token=token, key=JWT_TOKEN_SECRET_KEY, algorithms=[JWT_TOKEN_ALGORITHM])
        claims_rtx_id = claims.get("rtx_id")
        if not x_rtx_id or claims_rtx_id != x_rtx_id:
            raise JwtCredentialsException("The X-Rtx-Id credentials token is invalid.")
    except JWTError:
        raise credentials_exception

    return claims_rtx_id


description = """主要用于API的rtx-id获取，
直接重token解码获取，避免资源参数、查询参数、请求体参数、Header参数等传入的rtx-id不准，
也有verify_token_rtx方法，验证当前Token登录对象rtx-id与Header的rtx-id是否一致"""
@access.get("/token/me",
            summary="获取当前Token登录对象rtx-id",
            description=description
            )
async def jwt_token_me(
        token_user_rtx: str = Depends(decode_token_rtx)
):
    """
    获取当前Token登录对象rtx-id
    :param token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS.value,
        Status_enum.SUCCESS.value,
        Status_msg.get(100),
        {'decode_rtx_id': token_user_rtx}
    ).status_body


@access.get("/token/verify-me",
            summary="验证当前Token登录对象rtx-id与Header的rtx-id是否一致",
            description="比较解码Token对象data数据中的rtx-id与Header传入的rtx-id是否一致，如果不一致直接raise HTTPException，具体请查看verify_token_rtx方法源码")
async def jwt_token_verify_me(
        token_user_rtx: str = Depends(verify_token_rtx)
):
    """
    验证当前Token登录对象rtx-id与Header的rtx-id是否一致
    :param token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS.value,
        Status_enum.SUCCESS.value,
        Status_msg.get(100),
        {'verify_rtx_id': token_user_rtx}
    ).status_body

# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
