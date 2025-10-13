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

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from deploy.view import add_routers
from deploy.app_config.app_exception import register_app_exception  # app exception handle
from deploy.app_config.app_middleware import register_app_middleware    # app middleware

from deploy.utils.base_class import WebBaseClass
from deploy.utils.logger import logger as LOG
from deploy.config import SERVER_NAME, SERVER_VERSION, SERVER_DEBUG, \
    APP_OPENAPI_URL, APP_DOCS_URL, APP_REDOC_URL, \
    APP_STATIC_URL, APP_STATIC_ABS_DIR


# FastAPI App instance
app = FastAPI(
    # Docs配置[str类型，设置None为禁用状态]
    openapi_url=APP_OPENAPI_URL,
    docs_url=APP_DOCS_URL,
    redoc_url=None  # 禁用redoc_url
)


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

        # APP object configuration
        # ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -
        # 基础信息
        self.app.title = SERVER_NAME
        self.app.summary = "作者：高明亮"
        self.app.description = "Z2lisapi系统基于Python语言研发，使用FastAPI搭建的后端APIs。"     # 支持Markdown语法
        self.app.version = SERVER_VERSION
        # 开发配置
        self.app.debug = SERVER_DEBUG
        # 联系信息
        self.app.contact = {
            "name": "Pygo2",
            "url": "http://www.pygo2.top",
            "email": "gaoming971366@163.com"
        }

        # 静态资源
        self.app.mount(path=APP_STATIC_URL, app=StaticFiles(directory=APP_STATIC_ABS_DIR), name="static")
        # ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -

        # app middleware
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        register_app_middleware(app=app, app_headers=self.headers)
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

        # app webhook: exception_handler
        # -----------------------------------------------------------------------------------------------
        register_app_exception(app=app, app_headers=self.headers)
        # -----------------------------------------------------------------------------------------------

        # QRWebAppClass initialize
        super(QRWebAppClass, self).__init__()

        @app.on_event("startup")
        async def startup_event():
            LOG.info('>>>>> Web app startup success......')

        @app.on_event("shutdown")
        async def startup_shutdown():
            LOG.info('>>>>> Web app shutdown success......')

    def __str__(self):
        return "QRWebAppClass instance."

    def register_blueprint(self, router):
        """
        register router
        :param router: route object
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
