# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    access token

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
from fastapi import APIRouter, HTTPException, status as http_status, Depends, Header, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from deploy.reqbody.access import TokenBody as Token, O2LUserLogin
from deploy.utils.status import Status, SuccessStatus, FailureStatus
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code
from deploy.utils.utils import d2s
from deploy.utils.exception import JwtCredentialsException
from deploy.config import JWT_TOKEN_SECRET_KEY, JWT_TOKEN_ALGORITHM, JWT_TOKEN_EXPIRE_MINUTES
from deploy.service.access import AccessService


# view
access = APIRouter(prefix="/access", tags=["JWT Token系统验证"])
# service
access_service = AccessService()

TOKEN_DEFAULT_EXPIRE_MINUTES = 60 * 4  # 访问令牌过期时间，单位：分

# ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ *
"""
JWT Token地址配置
    > 方式一：OAuth2PasswordRequestForm组件表单：token_request_o_form
    > 方式二：From表单：token_request_form
    > 方式三：Request请求体：token 
    
线上API采用第三种方式设置oauth2_schema对象的tokenUrl
如果是Docs API文档验证模式，需要采用OAuth2PasswordRequestForm组件表单认证
"""
# 配置API oauth2_schema认证
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/access/token_request_o_form"
)

credentials_exception = HTTPException(
    http_status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@access.post("/token_request_o_form",
             response_model=Token,
             summary="用户Token API[OAuth2PasswordRequestForm组件表单] > Demo代码",
             description="依据用户[OAuth2PasswordRequestForm组件表单]提供的username，password参数（KEY不可更改），获取用户登录Token"
             )
async def access_token_request_o_form(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)) -> Status:
    """
    用户Token API
    :param form_data: OAuth2PasswordRequestForm组件表单
    :return: dict
    """
    username = getattr(form_data, "username", None)
    password = getattr(form_data, "password", None)
    if not username or not password:
        return FailureStatus(
            status_id=Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value
        )

    # TODO 用户校验
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return SuccessStatus(
        data={"access_token": token, "token_type": "Bearer"}
    )


@access.post("/token_request_form",
             response_model=Token,
             summary="用户Token API[Form表单] > Demo代码",
             description="依据用户[Form表单]提供的username，password参数（KEY不可更改），获取用户登录Token"
             )
async def access_token_request_from(
    username: str = Query(..., min_length=1, max_length=25, description="用户名称"),
    password: str = Query(..., min_length=1, max_length=30, description="用户密码")
) -> Status:
    """
    用户Token API
    :param username: Form表单对象
    :param password: Form表单对象
    :return: dict
    """
    if not username \
            or not password:
        return FailureStatus(
            status_id=Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value
        )

    # TODO 用户校验
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return SuccessStatus(
        data={"access_token": token, "token_type": "Bearer"}
    )


@access.post("/token_request_body",
             response_model=Token,
             summary="用户Token API[Request Body] > Demo代码",
             description="依据用户[Request Body]提供的username，password参数（KEY不可更改），获取用户登录Token"
             )
async def access_token_request_body(body_data: O2LUserLogin) -> Status:
    """
    用户Token API
    :param body_data: Request Body
    :return: dict
    """
    username = getattr(body_data, "username", None)
    password = getattr(body_data, "password", None)
    # 缺少登录参数
    if not username or not password:
        return FailureStatus(
            status_id=Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value
        )

    # TODO 用户校验
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return SuccessStatus(
        data={"access_token": token, "token_type": "Bearer"}
    )


# ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ *


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Token APIs:
    > create_access_token：创建Token
    > decode_token_rtx：解码Token
    > verify_token_rtx：验证Token

关键参数用户rtx-id
"""


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


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
验证Token APSs:
    > /token/me：Token解码
    > /token/verify-me：验证Headers与Token的RTX-ID是否是同一客户
    
如果需要在Docs API进行Token验证，oauth2_schema认证需要设置OAuth2PasswordRequestForm组件表单认证
"""

description = """主要用于API的rtx-id获取，
直接重token解码获取，避免资源参数、查询参数、请求体参数、Header参数等传入的rtx-id不准，
也有verify_token_rtx方法，验证当前Token登录对象rtx-id与Header的rtx-id是否一致"""


@access.get("/token-me",
            summary="获取当前Token登录对象rtx-id",
            description=description
            )
async def jwt_token_me(
        token_user_rtx: str = Depends(decode_token_rtx)
) -> Status:
    """
    获取当前Token登录对象rtx-id
    :param token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    return SuccessStatus(
        data={'decode_rtx_id': token_user_rtx}
    )


@access.get("/verify-me",
            summary="验证当前Token登录对象rtx-id与Header的rtx-id是否一致",
            description="比较解码Token对象data数据中的rtx-id与Header传入的rtx-id是否一致，如果不一致直接raise HTTPException，具体请查看verify_token_rtx方法源码"
            )
async def jwt_token_verify_me(
        token_user_rtx: str = Depends(verify_token_rtx)
) -> Status:
    """
    验证当前Token登录对象rtx-id与Header的rtx-id是否一致
    :param token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    return SuccessStatus(
        data={'verify_rtx_id': token_user_rtx}
    )

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


# * * * * * * * * * * * * * * * * * * * * * * * * * * [ APIs] * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
Open2lisapi APIs：
    > /2l/login：真实数据Login登录
"""


@access.post('/2l/login',
             summary="[Open2lisapi]Login登录",
             description="Open2lisapi后端APIs的login登录API，参数位username、password，用来登录获取用户信息、JWT-Token"
             )
async def open2lisapi_login(body_data: O2LUserLogin) -> Status:
    """
    Open2lisapi: Login登录
    :return: json data
    :param body_data: [dict]查询请求参数
    :return: json
    """
    username = getattr(body_data, "username", None).strip()     # 去空格
    password = getattr(body_data, "password", None)
    # 缺少登录参数
    if not username \
            or not password:
        return FailureStatus(
            Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value
        )

    # 用户信息核对
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    user = access_service.open2lisapi_login_rtx(rtx_id=username)
    # >>> user is not exist
    if not user:
        return FailureStatus(
            status_id=Status_code.CODE_201_LOGIN_USER_NOT_EXIST.value)
    # >>> user is deleted
    if user.get('is_del'):
        return FailureStatus(
            status_id=Status_code.CODE_203_LOGIN_USER_OFF.value)
    # >>> check password
    if user.get('password') != password:
        return FailureStatus(
            status_id=Status_code.CODE_204_LOGIN_USER_PASSWORD_ERROR.value)
    # 删除密码
    if user.get('password'):
        del user['password']
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # = = = = = = = = = = = = = = = = start token = = = = = = = = = = = = = = = =
    access_token_expires = timedelta(minutes=JWT_TOKEN_EXPIRE_MINUTES or TOKEN_DEFAULT_EXPIRE_MINUTES)
    token = create_access_token(
        data={"rtx_id": username, "apply_time": datetime.utcnow()},
        expires_delta=access_token_expires
    )
    # = = = = = = = = = = = = == = = = end token = = = = = == = = = = = = = = = =
    return SuccessStatus(
        data={"access_token": token, "token_type": "Bearer", "user": user}
    )


# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
