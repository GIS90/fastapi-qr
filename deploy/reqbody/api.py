# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    request body: api

base_info:
    __author__ = "PyGo"
    __time__ = "2024/9/3 22:20"
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
# usage: /usr/bin/python api.py
# ------------------------------------------------------------
from deploy.reqbody._base import baseModel
from pydantic import Field, field_validator
from typing import List, Tuple, Dict, Set, Optional, Union, Text


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
质量小程序APIs：
    ApiZlxcxProcessModel：过程检查
"""


class ApiZlxcxProcessModel(baseModel):
    """
    url: /zlxcx/process
    """
    xmbh: str = Field(..., min_length=1, max_length=8, description="项目编号")
    year: int = Field(..., ge=2023, le=10000, description="年份")
    quarter: str = Field(..., min_length=1, max_length=4, description="季度")

    class Config:
        json_schema_extra = {
            "example": {
                "xmbh": "1574",
                "year": 2023,
                "quarter": "第三季度"
            }
        }


# ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ * ～ *
"""
"""


