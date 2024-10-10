# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    method view
    方法类型：
        GET
        POST
        PUT
        DELETE
        HEAD
        OPTIONS
        PATCH

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/25 10:39"
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
# usage: /usr/bin/python method.py
# ------------------------------------------------------------
from fastapi import APIRouter, Query

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
method = APIRouter(prefix="/method", tags=["METHOD请求方法"])


@method.get('/get',
            summary="GET请求请求示例",
            description="GET请求请求示例"
            )
async def method_get(rtx_id: str):
    """
    GET请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'get'}
    ).status_body


@method.post('/post',
             summary="POST请求请求示例",
             description="POST请求请求示例"
             )
async def method_post(rtx_id: str):
    """
    POST请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'post'}
    ).status_body


@method.put('/put',
            summary="PUT请求请求示例",
            description="PUT请求请求示例"
            )
async def method_put(rtx_id: str):
    """
    PUT请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'put'}
    ).status_body


@method.delete('/delete',
               summary="DELETE请求请求示例",
               description="DELETE请求请求示例"
               )
async def method_delete(rtx_id: str):
    """
    DELETE请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'delete'}
    ).status_body


@method.head('/head',
             summary="HEAD请求请求示例",
             description="HEAD请求请求示例"
             )
async def method_head(rtx_id: str):
    """
    HEAD请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'head'}
    ).status_body


@method.options('/options',
                summary="OPTIONS请求请求示例",
                description="OPTIONS请求请求示例"
                )
async def method_options(rtx_id: str):
    """
    OPTIONS请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'options'}
    ).status_body


@method.patch('/patch',
              summary="PATCH请求请求示例",
              description="PATCH请求请求示例"
              )
async def method_patch(rtx_id: str):
    """
    PATCH请求请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {'rtx_id': rtx_id, 'method': 'patch'}
    ).status_body

# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
