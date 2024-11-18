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
# usage: /usr/bin/python base.py
# ------------------------------------------------------------
from deploy.body._base import baseModel
from pydantic import Field, validator, field_validator
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class Address(baseModel):
    """
    request body: Address
    Base model class
    """
    province: str = Field(..., min_length=1, max_length=25, description="省份")
    city: str = Field(..., min_length=1, max_length=120, description="省份")
    address: Optional[Text] = Field(default=None, min_length=0, max_length=120, description="详情地址")


class BaseUserBody(baseModel):
    """
    request body: User
    Base model class
    """
    name: str = Field(..., min_length=1, max_length=12, description="姓名")
    age: int = Field(..., ge=1, le=1000, description="年龄")
    sex: str = Field(..., min_length=1, max_length=1, description="性别")
    addr: Address

    class Config:
        json_schema_extra = {
            "example": {
                "name": "法外狂徒张三",
                "age": 32,
                "sex": "男",
                "addr": {
                    "province": "内蒙古",
                    "city": "兴安盟",
                    "address": "阿尔山温泉街道安居小区",
                }
            }
        }

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """
    name字段特殊验证
    """
    @field_validator("name")
    def name_is_alpha(cls, value: str):
        assert str(value).isalpha(), "name field is alpha."
        return value
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class UserBody(BaseUserBody):
    """
    request body: UserBody
    inherit BaseUser
    """
    phone: Optional[str] = Field(default=None, min_length=0, max_length=11, description="联系电话")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "法外狂徒张三",
                "age": 32,
                "sex": "男",
                "addr": {
                    "province": "内蒙古",
                    "city": "兴安盟",
                    "address": "阿尔山温泉街道安居小区",
                },
                "phone": ""
            }
        }


