# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2024/11/18 21:50"
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
# usage: /usr/bin/python response.py
# ------------------------------------------------------------
from deploy.reqbody._base import baseModel
from pydantic import Field, validator, field_validator, EmailStr
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class UserIn(baseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

    class Config:
        json_schema_extra = {
            "example": {
                "username": "法外狂徒张三",
                "password": "123456",
                "email": "gaoming@example.com",
                "full_name": "法外狂徒张三"
            }
        }


class UserOut(baseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

    class Config:
        json_schema_extra = {
            "example": {
                "username": "法外狂徒张三",
                "email": "gaoming@example.com",
                "full_name": "法外狂徒张三"
            }
        }
