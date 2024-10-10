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
from typing import List, Tuple, Dict, Set, Optional, Union
from fastapi import APIRouter, Request, Depends

from deploy.body.depend import BasePageBody
from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
depend = APIRouter(prefix="/depend", tags=["Depend依赖注入"])


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
函数依赖
"""
# 页面数据通用参数
async def page_common_parameters(parameter: BasePageBody) -> dict:
    return parameter.model_dump()


@depend.post('/depend',
             summary="[函数依赖]同步请求依赖注入",
             description="方法使用同步请求"
             )
def async_depend(page: dict = Depends(page_common_parameters)) -> dict:
    """
    :return: JSON
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {**page, **{"type": "同步请求"}}
    ).status_body


@depend.post('/async_depend',
             summary="[函数依赖]异步请求依赖注入",
             description="方法使用async异步请求"
             )
async def async_depend(page: dict = Depends(page_common_parameters)) -> dict:
    """
    :return: JSON
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {**page, **{"type": "异步请求"}}
    ).status_body


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
类依赖
"""
