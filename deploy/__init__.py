# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    QR = quick run
    app main class

    C-Middleware FastAPI Request:
        'app', 'auth', 'base_url', 'body', 'client', 'close', 'cookies', 'form', 'get', 'headers',
        'is_disconnected', 'items', 'json', 'keys', 'method', 'path_params', 'query_params', 'receive',
        'scope', 'send_push_promise', 'session', 'state', 'stream', 'url', 'url_for', 'user', 'values'

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 21:38"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:
    import uvicorn
    from deploy import create_app


    # supervisor>uvicorn startup(PROD)
    app = create_app()

design:
    Base FastAPI, use Singleton instance

reference urls:
    FastAPI: https://fastapi.tiangolo.com/
    中间件：https://www.itdocs.icu/fastapi/advanced/middleware/

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python __init__.py.py
# ------------------------------------------------------------
import sys
import time
from fastapi import FastAPI, Request, status as http_status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response, \
    PlainTextResponse, HTMLResponse, \
    JSONResponse, StreamingResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.encoders import jsonable_encoder

from deploy.view import add_routers
from deploy.utils.base_class import WebBaseClass
from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code
from deploy.utils.enums import MediaType
from deploy.utils.logger import logger as LOG
from deploy.config import APP_SECRET_KEY, APP_ALLOW_HOSTS, APP_CORS_ORIGINS, APP_M_ALLOW_HOSTS, \
    APP_M_GZIP_SIZE, APP_M_GZIP_LEVEL, APP_BAN_ROUTERS, APP_SESSION_MAX_AGE, \
    SERVER_NAME, SERVER_VERSION, SERVER_DEBUG


# FastAPI App instance
app = FastAPI()


class QRWebAppClass(WebBaseClass):
    """
    QRweb app class
    """
    app = None

    def __init__(self, app):
        """
        class initialize
        :param app: FastAPI App instance
        """
        self.app = app
        self.headers = {"app": "qr"}
        if not self.app:
            LOG.info('Web app server initialize is failure......')
            sys.exit(1)

        # app base config
        # ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -
        self.app.title = SERVER_NAME
        self.app.summary = "作者：高明亮"
        self.app.description = "基于FastAPI搭建的后端APIs，达到快速开发、上线的一款后台API脚手架项目。如果觉得还可以，欢迎点一个🌟支持一下，Thanks。"
        self.app.version = SERVER_VERSION
        self.app.docs_url = "/docs"
        self.app.redoc_url = "/redocs"
        self.app.debug = SERVER_DEBUG
        # ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -

        # app mount[挂载子应用SubAPP]
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # self.app.mount()
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # app middleware
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        # 自定义中间件C-Middleware
        @self.app.middleware("http")
        async def cm(request: Request, call_next):
            LOG.debug(">>>>> App middleware C-Middleware request")
            # - - - - - - - - - - - - - - - - 请求代码块 - - - - - - - - - - - - - - - -
            # [** 访问IP检查 **]
            if APP_ALLOW_HOSTS and \
                    request.client.host not in APP_ALLOW_HOSTS:
                content = Status(
                    Status_code.CODE_10000_EXCEPTION.value,
                    Status_enum.FAILURE.value,
                    f"IP not allow access: {request.client.host}",
                    {}
                ).status_body
                headers = {"webhook": "CM-IP"}
                headers.update(self.headers)
                return JSONResponse(
                    content=content,
                    status_code=http_status.HTTP_403_FORBIDDEN,
                    headers=headers,
                    media_type=MediaType.APPJson.value
                )

            # [** 资源请求地址检查 **]
            # TODO 子路径检查
            if request.url.path in APP_BAN_ROUTERS:
                content = Status(
                    Status_code.CODE_10000_EXCEPTION.value,
                    Status_enum.FAILURE.value,
                    f"Request resource is forbid: {request.url.path}",
                    {}
                ).status_body
                headers = {"webhook": "CM-PATH"}
                headers.update(self.headers)
                return JSONResponse(
                    content=content,
                    status_code=http_status.HTTP_403_FORBIDDEN,
                    headers=headers,
                    media_type=MediaType.APPJson.value
                )

            LOG.debug(">>>>> App middleware C-Middleware response")
            # + + + + + + + + + + + + + + + + 响应代码块 + + + + + + + + + + + + + + + +
            # [API执行时间]
            start = time.time()
            response = await call_next(request)
            end = time.time()
            response.headers["X-API-Process-Timer"] = str(end - start)
            response.headers["X-Mw"] = "C-Middleware"

            return response

        # 中间件 > CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=APP_CORS_ORIGINS or ["*"],  # 全部：["*"]
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

        # 中间件 > SESSION会话管理
        self.app.add_middleware(
            SessionMiddleware,
            secret_key=APP_SECRET_KEY or "910809ecb44c92db12ad5fa369375d00",    # md5 -qs mingliang.gao
            session_cookie="session",
            max_age=APP_SESSION_MAX_AGE or 15 * 24 * 60 * 60
        )

        # 中间件 > HTTPSRedirectMiddleware(强制所有传入请求必须是 https 或 wss)
        # self.app.add_middleware(HTTPSRedirectMiddleware)

        # 中间件 > TrustedHost
        """
        # C-Middleware自定义中间件中定义了IP检查
        self.app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=APP_M_ALLOW_HOSTS  # hosts list, [ip, domain]
        )
        """

        # 中间件 > GZip
        self.app.add_middleware(
            GZipMiddleware,
            minimum_size=APP_M_GZIP_SIZE,  # default 500byte
            compresslevel=APP_M_GZIP_LEVEL  # default 9
        )
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

        # app webhook: exception_handler
        # -----------------------------------------------------------------------------------------------
        # HTTPException
        @self.app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exec: HTTPException):
            """
            :param request: Request
            :param exec: HTTPException
            :return: JSONResponse
            """
            # rewrite response
            content = Status(
                Status_code.CODE_901_HTTP_EXCEPTION.value,
                Status_enum.FAILURE.value,
                Status_msg.get(901),
                {"error": exec.detail}
            ).status_body
            headers = {"webhook": "HTTPException"}
            headers.update(self.headers)
            return JSONResponse(
                content=content,
                status_code=http_status.HTTP_200_OK,
                headers=headers,
                media_type=MediaType.APPJson.value
            )

        # RequestValidationError
        @self.app.exception_handler(RequestValidationError)
        async def request_validation_error(request: Request, exec: RequestValidationError):
            """
            :param request: Request
            :param exec: RequestValidationError
            :return: JSONResponse
            """
            # rewrite response >>> 加入请求体body
            content = Status(
                Status_code.CODE_404_REQUEST_PARAMETER_VALUE_ERROR.value,
                Status_enum.FAILURE.value,
                "请求参数错误" or Status_msg.get(404),
                jsonable_encoder({"error": exec.errors()})   # jsonable_encoder({"error": exec.errors(), "body": exec.body})   # 返回请求体参数 + errors
            ).status_body
            headers = {"webhook": "RequestValidationError"}
            headers.update(self.headers)
            return JSONResponse(
                content=content,
                status_code=http_status.HTTP_200_OK,
                headers=headers,
                media_type=MediaType.APPJson.value
            )
        # -----------------------------------------------------------------------------------------------

        # QRWebAppClass initialize
        super(QRWebAppClass, self).__init__()

    def register_blueprint(self, router):
        """
        register router
        :param router: router object
            contain prefix, tags, response and so on...
        :return: None
        """
        if router:
            LOG.info(f'Blueprint {router.prefix} is register')
            self.app.include_router(router)

    def _auto_register_blueprint(self):
        for route in add_routers:
            if not route: continue
            self.register_blueprint(router=route)

    def init_run(self):
        """
        web app initialize
        :return: None
        """
        LOG.info('Web app server start initialize......')
        self._auto_register_blueprint()
        LOG.info('Web app server end initialize......')


def create_app():
    return QRWebAppClass(app).app
