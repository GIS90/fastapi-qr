# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    upload view

    File、UploadFile区别：
        - 文件大小：File适合小文件；UploadFile适合大文件，比如视频
        - 文件属性：File上传的为bytes，无属性；UploadFile上传的文件具有文件属性，比如创建时间、创建用户、修改时间等
        - 异步：File不支持异步操作；UploadFile支持异步操作
        - 接收类型：File为bytes；UploadFile为UploadFile对象
        - 文件对象：UploadFile上传的文件是Python文件对象，支持write(), read(), seek(), close()等文件流操作
        - 写入操作：UploadFile存储在内存的文件超出最大上限时，会把文件存入磁盘

    上传文件推荐使用UploadFile

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/23 10:43"
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
# usage: /usr/bin/python upload.py
# ------------------------------------------------------------
from fastapi import APIRouter, status as http_status, \
    File, UploadFile
from typing import Optional, Union, List, Tuple, Dict

from deploy.service.upload import UploadService
from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
upload = APIRouter(prefix='/upload', tags=["文件上传"])


# define serice
upload_service = UploadService()


@upload.post('/file',
             summary="File单个小文件上传",
             description="单个小文件上传，File也有很多参数，目前来说通过file对象获取不到文件的名称等属性，具体查看源码，不推荐使用"
             )
async def file_api(
        file: bytes = File(...)
) -> dict:
    """
    File单个小文件上传
    :param file: [File]File文件对象
    :return: json
    """
    return upload_service.file_api(file)


@upload.post('/files',
             summary="File多个小文件上传",
             description="多个小文件上传，使用的就是List，其中元素都是File对象，不推荐使用")
async def files_api(
        files: List[bytes] = File(...)
) -> dict:
    """
    File单个多文件上传
    :param files: [list]File文件对象列表
    :return: json
    """
    result = list()
    for f in files:
        if not f: continue
        res = upload_service.file_api(file=f)
        if res.get('status_id'):
            result.append(res.get('data').get('file'))

    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {"file-list": result, "file-count": len(result)}
    ).status_body


@upload.post('/upload_file',
             summary="UploadFile单个大文件上传",
             description="单个大文件上传，UploadFile对象可以获取文件属性，具体参数请查看UploadFile源码，推荐使用")
async def upload_file(
        file: UploadFile = File(...)
) -> dict:
    """
    UploadFile单个大文件上传
    :param file: [UploadFile]UploadFile上传文件对象
    :return: json
    """
    return await upload_service.upload_file_api(file)


@upload.post('/upload_files',
             summary="UploadFile多个大文件上传",
             description="多个大文件上传，UploadFile对象可以获取文件属性，具体参数请查看UploadFile源码，推荐使用")
async def upload_files(
        files: List[UploadFile] = File(...)
) -> dict:
    """
    UploadFile多个大文件上传
    :param files: [UploadFile]UploadFile上传文件对象集合
    :return: json
    """
    result = list()
    for f in files:
        if not f: continue
        res = await upload_service.upload_file_api(file=f)
        if res.get('status_id'):
            result.append(res.get('data').get('file'))
    return Status(
        Status_code.CODE_100_SUCCESS,
        Status_enum.SUCCESS,
        Status_msg.get(100),
        {"file-list": result, "file-count": len(result)}
    ).status_body

# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
