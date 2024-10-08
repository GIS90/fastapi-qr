# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    upload service

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/25 23:06"
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
import os
from datetime import datetime
from fastapi import File, UploadFile
from pathlib import Path as pathlib_path, PurePath as pathlib_purep
from deploy.utils.utils import get_root_folder, d2s
from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# 定一个临时文件存储abs路径
abs_store_folder = pathlib_path.joinpath(get_root_folder(), 'deploy/static')


class UploadService(object):
    """
    upload service
    """
    # 定义文件读取默认大小
    READ_SIZE = 1024 * 1024  # 1024 = 1KB

    def __init__(self):
        """
        ApisService class initialize
        """
        super(UploadService, self).__init__()

    def __str__(self):
        print("UploadService class.")

    def __repr__(self):
        self.__str__()

    def file_api(self, file: File) -> dict:
        """
        File单个小文件上传
        :param file: [File]File文件对象
        :return:
        """
        if not file:
            return Status(
                Status_code.CODE_450_REQUEST_FILE_NO_UPLOAD,
                Status_enum.FAILURE,
                Status_msg.get(450),
                {}
            ).status_body

        file_name = d2s(datetime.now())  # custom define upload file name
        real_file = pathlib_path.joinpath(abs_store_folder, file_name)
        if pathlib_path.exists(real_file):
            print(f'{real_file} is exist, remove...........')
            os.remove(real_file)
        # - - - - - - - - - - - - - write file - - - - - - - - - - - - -
        with open(real_file, 'wb') as f:
            f.write(file)
        return Status(
            Status_code.CODE_100_SUCCESS,
            Status_enum.SUCCESS,
            Status_msg.get(100),
            {"file": real_file}
        ).status_body

    async def upload_file_api(self, file: UploadFile) -> dict:
        """
        UploadFile单个大文件上传
        :param file: [UploadFile]UploadFile上传文件对象
        :return: json
        """
        if not file:
            return Status(
                Status_code.CODE_450_REQUEST_FILE_NO_UPLOAD,
                Status_enum.FAILURE,
                Status_msg.get(450),
                {}
            ).status_body

        file_name = getattr(file, 'filename')  # use getattr method to get file name
        if not file_name:
            file_name = d2s(datetime.now())
        real_file = pathlib_path.joinpath(abs_store_folder, file_name)
        if pathlib_path.exists(real_file):
            print(f'{real_file} is exist, remove...........')
            os.remove(real_file)
        # - - - - - - - - - - - - - write file - - - - - - - - - - - - -
        with open(real_file, "wb") as f:
            while content := await file.read(self.READ_SIZE):
                f.write(content)
        return Status(
            Status_code.CODE_100_SUCCESS,
            Status_enum.SUCCESS,
            Status_msg.get(100),
            {"file": real_file}
        ).status_body
