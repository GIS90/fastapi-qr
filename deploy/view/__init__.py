# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    view

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 21:39"
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
# usage: /usr/bin/python __init__.py.py
# ------------------------------------------------------------
from deploy.view.base import base
from deploy.view.method import method
from deploy.view.access import access
from deploy.view.verify import verify
from deploy.view.upload import upload
from deploy.view.error import error
from deploy.view.response import response
from deploy.view.api import api


__all__ = ["add_routers"]


add_routers = [
    base,
    method,
    access,
    verify,
    upload,
    error,
    response,
    api,
]
