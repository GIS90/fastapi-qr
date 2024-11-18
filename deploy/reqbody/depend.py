# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    depend body

base_info:
    __author__ = "PyGo"
    __time__ = "2024/10/10 22:43"
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
from deploy.reqbody._base import baseModel
from pydantic import Field
from typing import List, Tuple, Dict, Set, Optional, Union, Text


class BasePageBody(baseModel):
    """
    Base Page body
    """
    page: int = Field(..., ge=1, le=10000, description="页码")
    limit: int = Field(..., ge=1, le=10000, description="条数")

    class Config:
        json_schema_extra = {
            "example": {
                "page": 1,
                "limit": 15
            }
        }


class PageLikeBody(BasePageBody):
    """
    Page filter like body
    inherit BaseUser
    """
    search: Optional[Text] = Field(default=None,  min_length=0, max_length=55, description="模糊查询信息")

    class Config:
        json_schema_extra = {
            "example": {
                "page": 1,
                "limit": 15,
                "search": "你是我的唯一。。。。。。。。"
            }
        }
