# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    api view

base_info:
    __author__ = "PyGo"
    __time__ = "2024/8/21 21:45"
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
# usage: /usr/bin/python zlxcx.py
# ------------------------------------------------------------
from fastapi import APIRouter, Query, Request

from deploy.utils.status import Status, SuccessStatus
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code

from deploy.reqbody.api import ApiZlxcxProcessModel
from deploy.service.api import ApiService


# define view
api = APIRouter(prefix="/api", tags=["APIs集合"])
api_service = ApiService()


@api.post('/zlxcx/process',
          summary="[质量小程序APIs]过程检查",
          description="项目过程检查的详情数据"
          )
async def zlxcx_process(params: ApiZlxcxProcessModel) -> dict:
    """
    质量小程序: 过程检查
    :return: json data
    :param params: [dict]查询请求参数
    :return: json
    """
    return api_service.zlxcx_process(params.model_dump())
