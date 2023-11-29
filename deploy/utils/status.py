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
from deploy.utils.status_value import StatusMsg


class Status(object):
    def __init__(self, status_id: int, status: str, msg: str, data=None):
        if data is None:
            data = {}
        self.status_body = {
            "status_id": status_id,
            "status": status,
            "message": msg if msg else StatusMsg.get(status_id),
            "data": data,
        }
        self.data = data
        super(Status, self).__init__()

    def json(self):
        return json.dumps(self.status_body)

