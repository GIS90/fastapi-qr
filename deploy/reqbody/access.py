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
from pydantic import Field, field_validator
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class O2LUserLogin(baseModel):
    """
    url: /2l/login
    """
    username: str = Field(..., min_length=1, max_length=25, description="用户名称")
    password: str = Field(..., min_length=1, max_length=30, description="用户密码")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "adc",
                "password": "123456"
            }
        }

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """
    username字段特殊验证：字母+数字
    """
    @field_validator("username")
    def name_is_alnum(cls, value: str):
        assert str(value).isalnum(), "username field is isalnum."
        return value
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class TokenBody(baseModel):
    """
    Token body
    """
    access_token: str
    token_type: str
