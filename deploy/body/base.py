# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    base view body

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/23 22:06"
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
# usage: /usr/bin/python basev.py
# ------------------------------------------------------------
from deploy.body._base import baseModel
from pydantic import Field
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class BaseUserBody(baseModel):
    """
    Base User body
    """
    name: str = Field(..., min_length=1, max_length=12, description="姓名")
    age: int = Field(..., gt=1, lt=1000, description="年龄")
    sex: str = Field(..., min_length=1, max_length=1, description="性别")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "法外狂徒张三",
                "age": 32,
                "sex": "男"
            }
        }


class UserBody(BaseUserBody):
    """
    User body
    inherit BaseUser
    """
    phone: Optional[str] = Field(default=None, min_length=0, max_length=11, description="联系电话")
    address: Optional[Text] = Field(default=None,  min_length=0, max_length=120, description="现居地址")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "法外狂徒张三",
                "age": 32,
                "sex": "男",
                "phone": "",
                "address": "地球"
            }
        }


