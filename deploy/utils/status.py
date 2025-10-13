# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    the class of response
    type: json
    to use api

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 22:33"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:
    Status(
        101,
        'failure',
        u'Server发生错误，获取失败',
        {}
    ).json()

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python status.py
# ------------------------------------------------------------
import json
from fastapi import status as http_status
from fastapi.responses import JSONResponse
from typing import Union, Dict, List

from deploy.utils.status_value import StatusCode, StatusMsg
from deploy.utils.enum import MediaType


class Status(JSONResponse):
    def __init__(self, status_id: int, message: str, data: Union[List, Dict] = None):
        if data is None:
            data = {}
        self.status_body = {
            "status_id": status_id,
            "message": message if message else StatusMsg.get(status_id),
            "data": data,
        }
        super().__init__(
            content=self.status_body,
            status_code=http_status.HTTP_200_OK,
            media_type=MediaType.APPJson.value
        )

    def json(self):
        return json.dumps(self.status_body)

    def dict(self):
        return self.status_body


class SuccessStatus(Status):
    """
    成功
    """

    def __init__(self,
                 status_id: int = StatusCode.CODE_100_SUCCESS.value,
                 message: str = None,
                 data: Union[List, Dict] = None
                 ):

        super().__init__(status_id, message, data)


class FailureStatus(Status):
    """
    失败
    """

    def __init__(self,
                 status_id: int = StatusCode.CODE_900_SERVER_API_EXCEPTION.value,
                 message: str = None,
                 data: Union[List, Dict] = None
                 ):

        super().__init__(status_id, message, data)
