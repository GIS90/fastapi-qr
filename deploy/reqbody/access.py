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
from deploy.reqbody._base import baseModel
from pydantic import Field
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class LoginBody(baseModel):
    """
    Token body
    """
    username: str = Field(..., min_length=1, max_length=55, description="用户名称")
    password: str = Field(..., min_length=1, max_length=55, description="用户密码")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "法外狂徒张三",
                "password": "我是一个汉字的密码"
            }
        }


class TokenBody(baseModel):
    """
    Token body
    """
    access_token: str
    token_type: str
