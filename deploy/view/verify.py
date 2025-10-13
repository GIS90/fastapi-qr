# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    verify view

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/25 15:57"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python verify.py
# ------------------------------------------------------------
from fastapi import APIRouter, Depends, Request, Header

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code
from deploy.view.access import decode_token_rtx, verify_token_rtx
from deploy.reqbody.base import UserBody


# define view
verify = APIRouter(prefix="/verify", tags=["指定Router全局使用JWT Token验证"], dependencies=[Depends(verify_token_rtx)])

verify_description = """
API利用Token进行验证，很多API都是在资源参数/查询参数/Header/请求体参数中传入的rtx-id用来校验，
这里直接在Router中进行用户校验Token依赖注入，利用verify_token_rtx来进行验证传入的与解码Token的rtx-id是否一致，具体的源码请查看verify_token_rtx方法，
如果想用Token解码获取rtx-id，直接用decode_token_rtx。

目前有一个问题：在全局Router中注入dependencies依赖，暂时没有获取到全局dependencies的返回值
"""


@verify.get("/v1",
            summary="校验Token的rtx-id数据，V1示例：无请求体参数",
            description=verify_description)
async def verify_v1(request: Request) -> dict:
    """
    token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """调用service业务逻辑代码"""
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        "依赖注入全局Router：Token与传入rtx-id校验通过了" or Status_msg.get(100),
        {}
    ).status_body


@verify.post("/v2",
             summary="校验Token的rtx-id数据，V2示例：有请求体参数",
             description=verify_description)
async def verify_v2(
        user: UserBody,
        x_rtx_id: str = Header(..., min_length=1, max_length=25, convert_underscores=True, description="X-Token")
) -> dict:
    """
    token_user_rtx: [str]当前Token登录对象rtx-id
    :return: json
    """
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """调用service业务逻辑代码"""
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        "依赖注入全局Router：Token与传入rtx-id校验通过了" or Status_msg.get(100),
        {**user.model_dump(), **{"x-rtx-id": x_rtx_id}}
    ).status_body
# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
