# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    error view

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/23 10:43"
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
# usage: /usr/bin/python error.py
# ------------------------------------------------------------
from fastapi import APIRouter, HTTPException, status as http_status
from fastapi.exceptions import RequestValidationError

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
error = APIRouter(prefix="/error", tags=["ERROR错误"])


@error.get('/http_exception/404',
           summary="自定义HTTPException**[404]**异常处理",
           description="基于Fastapi的HTTPException，返回response，HTTPException包含status_code、detail、headers内容，"
                       "status_code是状态码，detail是具体内容，headers请求头。在app中可以设置全局exception_handler，具体可以参考deploy/__init__.py文件的app初始化配置。"
           )
async def http_exception(
        exec: bool = False
):
    """
    自定义HTTPException异常处理 > HTTP_404_NOT_FOUND
    :param exec: 是否触发异常
    :return: json
    """
    if exec:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail="http_exception [HTTP_404_NOT_FOUND] detail ..............................................",
            headers={"error": "HTTP_404_NOT_FOUND"}
        )

    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {"error": "http_exception [HTTP_404_NOT_FOUND]"}
    ).status_body


@error.get('/http_exception/500',
           summary="自定义HTTPException**[500]**异常处理"
           )
async def http_exception(
    exec: bool = False
):
    """
    自定义HTTPException异常处理 > HTTP_500_INTERNAL_SERVER_ERROR
    :param exec: 是否触发异常
    :return: json
    """
    if exec:
        raise HTTPException(
            status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="http_exception [HTTP_500_INTERNAL_SERVER_ERROR] detail ..............................................",
            headers={"error": "HTTP_500_INTERNAL_SERVER_ERROR"}
        )

    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {"error": "http_exception [HTTP_500_INTERNAL_SERVER_ERROR]"}
    ).status_body


@error.get('/request_valid_error',
           summary="自定义RequestValidationError异常处理"
           )
async def request_valid_error(
    exec: bool = False
):
    """
    自定义RequestValidationError异常处理
    :param exec: 是否触发异常
    :return: json

    status_code = 422
    """
    if exec:
        raise RequestValidationError(
            errors={"errors": "RequestValidationError"},
        )

    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {}
    ).status_body

# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
