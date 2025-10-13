# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    app middleware

base_info:
    __author__ = "PyGo"
    __time__ = "2024/12/23 22:42"
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
# usage: /usr/bin/python app_middleware.py
# ------------------------------------------------------------
import time

from fastapi import FastAPI, Request, status as http_status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware

from deploy.utils.status_value import StatusMsg as Status_msg, \
    StatusCode as Status_code
from deploy.utils.status import FailureStatus
from deploy.utils.enum import MediaType
from deploy.utils.logger import logger as LOG
from deploy.config import APP_SECRET_KEY, APP_ALLOW_HOSTS, APP_CORS_ORIGINS, APP_M_ALLOW_HOSTS, \
    APP_M_GZIP_SIZE, APP_M_GZIP_LEVEL, APP_BAN_ROUTERS, APP_SESSION_MAX_AGE, APP_REQUEST_METHODS, \
    NON
from deploy.utils.token import verify_access_token_expire


def register_app_middleware(app: FastAPI, app_headers: dict):
    """
    App中间件
    """

    # app middleware
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """
    自定义中间件C-Middleware:
        - 访问IP检查
        - 资源请求地址检查
        - 请求方法检查
        - Jwt Token验证
    """
    @app.middleware("http")
    async def cmAccess(request: Request, call_next):
        LOG.debug(">>>>> App middleware C-Middleware request")
        is_verify_token = False  # 是否验证Jwt Token有效性[默认验证]

        # - - - - - - - - - - - - - - - - 请求代码块 - - - - - - - - - - - - - - - -
        # [** 访问IP检查 **]
        if APP_ALLOW_HOSTS and \
                request.client.host not in APP_ALLOW_HOSTS:
            content = FailureStatus(
                status_id=Status_code.CODE_10001_BAN_REQUEST.value,
                message=f"IP not allow access: {request.client.host}"
            ).status_body
            headers = {"X-App-CM-Request-Webhook": "CM-IP"}
            headers.update(app_headers)
            return JSONResponse(
                content=content,
                status_code=http_status.HTTP_200_OK,
                headers=headers,
                media_type=MediaType.APPJson.value
            )

        # [** 资源请求地址检查 **]
        if APP_BAN_ROUTERS and \
                request.url.path in APP_BAN_ROUTERS:
            content = FailureStatus(
                status_id=Status_code.CODE_10001_BAN_REQUEST.value,
                message=f"Request resource is forbid: {request.url.path}"
            ).status_body
            headers = {"X-App-CM-Request-Webhook": "CM-PATH"}
            headers.update(app_headers)
            return JSONResponse(
                content=content,
                status_code=http_status.HTTP_200_OK,
                headers=headers,
                media_type=MediaType.APPJson.value
            )

        # [** 请求方法 **]
        if APP_REQUEST_METHODS and \
                str(request.method).upper() not in APP_REQUEST_METHODS:
            content = FailureStatus(
                status_id=Status_code.CODE_300_REQUEST_METHOD_ERROR.value,
                message=f"Request method is error: {request.url.path}"
            ).status_body
            headers = {"X-App-CM-Request-Webhook": "CM-METHOD"}
            headers.update(app_headers)
            return JSONResponse(
                content=content,
                status_code=http_status.HTTP_200_OK,
                headers=headers,
                media_type=MediaType.APPJson.value
            )

        # [** Jwt Token验证 **]
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        """
        通过请求Headers获取X-Token、X-Rtx-Id信息，验证用户是否Token有效性
        注意：Header请求参数KEY需要采用[驼峰+中划线]方法命令
        """
        """
        no check jwt token request condition
          - api: rest open apis, special api for blueprints
          - access: login in and login out APIs
        """
        if request.url.path == "/" or \
                request.url.path.startswith("/api/") or \
                request.url.path.startswith("/access/"):
            is_verify_token = False

        token_rtx_id = None
        if is_verify_token:
            request_token = request.headers.get('X-Token')
            # request_rtx_id = request.headers.get('X-Rtx-Id')
            headers = {"X-App-CM-Request-Webhook": "CM-TOKEN"}
            headers.update(app_headers)
            # NO Token
            if not request_token:
                content = FailureStatus(
                    status_id=Status_code.CODE_250_TOKEN_NOT_FOUND.value,
                    message=Status_msg.get(250)
                ).status_body
                return JSONResponse(
                    content=content,
                    status_code=http_status.HTTP_200_OK,
                    headers=headers,
                    media_type=MediaType.APPJson.value
                )
            # Token expire
            expire, token_rtx_id = verify_access_token_expire(x_token=request_token)
            if expire:
                content = FailureStatus(
                    status_id=Status_code.CODE_253_TOKEN_EXPIRE.value,
                    message=Status_msg.get(253)
                ).status_body
                return JSONResponse(
                    content=content,
                    status_code=http_status.HTTP_200_OK,
                    headers=headers,
                    media_type=MediaType.APPJson.value
                )
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

        LOG.debug(">>>>> App middleware C-Middleware response")
        # + + + + + + + + + + + + + + + + 响应代码块 + + + + + + + + + + + + + + + +
        # [API Watcher执行时间]
        start = time.time()
        response = await call_next(request)
        end = time.time()
        cost = end - start

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
        """ 
        [watcher]
        > [ 在CM中对有Token请求的进行了watcher request ]
        > access在方法中直接调用user_service.request
        > APIs做成装饰器进行watcher request
        """
        if is_verify_token:
            pass
            # 验证用户可用性
            '''
            from deploy.service.user import UserService
            user_service = UserService()
            await user_service.request(rtx_id=token_rtx_id or O_NOBN, request_body=request, cost=cost)
            '''
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

        response.headers["X-App-CM-Timer"] = str(cost)
        response.headers["X-App-CM-Response-Webhook"] = "C-Middleware-Timer"
        for _k, _v in app_headers.items():
            if not _k: continue
            response.headers[_k] = _v

        LOG.debug("<<<<< App middleware C-Middleware response")
        LOG.debug("<<<<< App middleware C-Middleware request")

        return response

    # 中间件 > CORS跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=APP_CORS_ORIGINS or ["*"],  # 全部：["*"]
        allow_credentials=True,  # 认证
        allow_methods=["*"],  # 方法
        allow_headers=["*"]  # Headers信息
    )

    # 中间件 > SESSION会话管理
    app.add_middleware(
        SessionMiddleware,
        secret_key=APP_SECRET_KEY,
        session_cookie="session",
        max_age=APP_SESSION_MAX_AGE or 15 * 24 * 60 * 60
    )

    # 中间件 > HTTPSRedirectMiddleware(强制所有传入请求必须是 https 或 wss)
    """
    self.app.add_middleware(HTTPSRedirectMiddleware)
    """

    # 中间件 > TrustedHost
    """
    # C-Middleware自定义中间件中定义了IP检查
    self.app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=APP_M_ALLOW_HOSTS  # hosts list, [ip, domain]
    )
    """

    # 中间件 > GZip
    app.add_middleware(
        GZipMiddleware,
        minimum_size=APP_M_GZIP_SIZE,  # default 500byte
        compresslevel=APP_M_GZIP_LEVEL  # default 9
    )
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
