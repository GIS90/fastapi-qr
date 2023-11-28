# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/28 20:57"
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
# usage: /usr/bin/python __bo_template.py
# ------------------------------------------------------------
from sqlalchemy import distinct, func

from deploy.bo.bo_base import BOBase
# from deploy.models.XXXXX import


class ModelBo(BOBase):

    def __init__(self):
        super(ModelBo, self).__init__()

    def __str__(self):
        return "Model Bo."

    def __repr__(self):
        return self.__str__()

    # def new_mode(self):
        # return ModelBo()
