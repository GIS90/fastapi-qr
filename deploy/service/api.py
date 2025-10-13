# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2024/9/3 22:25"
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
import requests

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


class ApiService(object):
    """
    API Service
    """

    # zlxcx_process
    zlxcx_process_params = [
        'xmbh',
        'year',
        'quarter'
    ]
    ZLXCX_PROCESS_YEAR_LIST = [2023, 2024]
    ZLXCX_PROCESS_QUARTER_LIST = {
        "第一季度": 0,
        "第二季度": 1,
        "第三季度": 2,
        "第四季度": 3,
    }

    def __init__(self):
        """
        ApiService class initialize
        """
        super(ApiService, self).__init__()

    def __str__(self):
        print("ZlxcxService class.")

    def __repr__(self):
        self.__str__()

    def zlxcx_token(self) -> dict:
        return {"token": "ABC"}

    def zlxcx_process(self, params: dict) -> dict:
        """
        质量小程序: 过程检查
        :return: json data
        """

        return params

