# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    app exception

base_info:
    __author__ = "PyGo"
    __time__ = "2024/12/23 22:22"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "z2lisapi"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life every day！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python app_exception.py
# ------------------------------------------------------------
from fastapi import FastAPI, Request, status as http_status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from deploy.utils.status_value import StatusMsg as Status_msg, \
    StatusCode as Status_code
from deploy.utils.status import FailureStatus
from deploy.utils.exception import JwtCredentialsException, UserInValidateException
from deploy.utils.enum import MediaType
from deploy.config import SERVER_DEBUG
from deploy.utils.logger import logger as LOG


def register_app_exception(app: FastAPI, app_headers: dict):
    """
    App异常捕捉
    """

    # RequestValidationError[请求验证错误]
    @app.exception_handler(RequestValidationError)
    async def request_validation_error(request: Request, exec: RequestValidationError):
        """
        :param request: Request
        :param exec: RequestValidationError
        :return: JSONResponse
        """
        if SERVER_DEBUG:
            print(f"请求地址{request.url.__str__()}，[request_validation_error]: {exec.errors()}")
        LOG.exception(exec)

        # rewrite response >>> 加入请求体body
        content = FailureStatus(
            status_id=Status_code.CODE_404_REQUEST_PARAMETER_VALUE_ERROR.value,
            message="请求参数错误" or Status_msg.get(404),
            data=jsonable_encoder({"error": exec.errors()})  # jsonable_encoder({"error": exec.errors(), "body": exec.body})   # 返回请求体参数 + errors
        ).status_body
        headers = {"app-cm-exception-webhook": "RequestValidationError"}
        headers.update(app_headers)
        return JSONResponse(
            content=content,
            status_code=http_status.HTTP_200_OK,
            headers=headers,
            media_type=MediaType.APPJson.value
        )

    # JwtCredentialsException[Jwt Token验证异常]
    @app.exception_handler(JwtCredentialsException)
    async def jwt_exception_handler(request: Request, exec: JwtCredentialsException):
        """
        :param request: Request
        :param exec: JwtCredentialsException
        :return: JSONResponse
        """
        if SERVER_DEBUG:
            print(f"请求地址{request.url.__str__()}，[jwt_exception_handler]: {exec.__str__()}")
        LOG.exception(exec)

        # rewrite response
        content = FailureStatus(
            status_id=Status_code.CODE_251_TOKEN_VERIFY_FAILURE.value,
            message=Status_msg.get(251),
            data={"error": exec.detail}
        ).status_body
        headers = {"app-cm-exception-webhook": "JwtCredentialsException"}
        headers.update(app_headers)
        return JSONResponse(
            content=content,
            status_code=http_status.HTTP_200_OK,
            headers=headers,
            media_type=MediaType.APPJson.value
        )

    # UserInValidateException[用户不可用验证异常]
    @app.exception_handler(UserInValidateException)
    async def user_invalid_exception_handler(request: Request, exec: UserInValidateException):
        """
        :param request: Request
        :param exec: UserInValidateException
        :return: JSONResponse
        """
        if SERVER_DEBUG:
            print(f"请求地址{request.url.__str__()}，[user_invalid_exception_handler]: {exec.__str__()}")
        LOG.exception(exec)

        # rewrite response
        content = FailureStatus(
            status_id=Status_code.CODE_207_USER_INVALID.value,
            message=Status_msg.get(207),
            data={"error": exec.detail}
        ).status_body
        headers = {"app-cm-exception-webhook": "UserInValidateException"}
        headers.update(app_headers)
        return JSONResponse(
            content=content,
            status_code=http_status.HTTP_200_OK,
            headers=headers,
            media_type=MediaType.APPJson.value
        )

    # HTTPException[HTTP异常]
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exec: HTTPException):
        """
        :param request: Request
        :param exec: HTTPException
        :return: JSONResponse
        """
        if SERVER_DEBUG:
            print(f"请求地址{request.url.__str__()}，[http_exception_handler]: {exec.__str__()}")
        LOG.exception(exec)

        # rewrite response
        content = FailureStatus(
            status_id=Status_code.CODE_901_HTTP_EXCEPTION.value,
            message=Status_msg.get(901),
            data={"error": exec.__str__()}
        ).status_body
        headers = {"app-cm-exception-webhook": "HTTPException"}
        headers.update(app_headers)
        return JSONResponse(
            content=content,
            status_code=http_status.HTTP_200_OK,
            headers=headers,
            media_type=MediaType.APPJson.value
        )

    # [Exception验证异常]
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exec: Exception):
        """
        :param request: Request
        :param exec: Exception
        :return: JSONResponse
        """
        if SERVER_DEBUG:
            print(f"请求地址{request.url.__str__()}，[all_exception_handler]: {exec.__str__()}")
        LOG.exception(exec)

        # rewrite response
        content = FailureStatus(
            status_id=Status_code.CODE_900_SERVER_API_EXCEPTION.value,
            message=Status_msg.get(900),
            data={"error": exec.__str__()}
        ).status_body
        headers = {"app-cm-exception-webhook": "Exception"}
        headers.update(app_headers)
        return JSONResponse(
            content=content,
            status_code=http_status.HTTP_200_OK,
            headers=headers,
            media_type=MediaType.APPJson.value
        )
