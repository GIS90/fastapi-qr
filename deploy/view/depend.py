# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    depend
    依赖的好处：
        1、提高代码的复用率
        2、共享数据库连接
        3、增强安全、认证、角色管理

base_info:
    __author__ = "PyGo"
    __time__ = "2024/10/10 22:21"
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
# usage: /usr/bin/python depend.py
# ------------------------------------------------------------
from fastapi import APIRouter, Request

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
depend = APIRouter(prefix="/depend", tags=["Depend依赖注入"])


@depend.get('/',
          summary="Welcome to FastAPI-QR脚手架",
          description="Hello FastAPI-QR脚手架!"
          )
async def hi():
    """
    :return: JSON
    """
