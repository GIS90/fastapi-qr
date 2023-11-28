# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    access body

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/25 11:02"
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
# usage: /usr/bin/python access.py
# ------------------------------------------------------------
from deploy.body.base import baseModel


class TokenBody(baseModel):
    """
    Token body
    """
    access_token: str
    token_type: str
