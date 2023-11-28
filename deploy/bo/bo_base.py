# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/28 20:56"
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
# usage: /usr/bin/python bo_base.py
# ------------------------------------------------------------

from deploy.model.base import get_session


class BOBase(object):

    def __init__(self, model=None):
        self.session = get_session()
        self.model = model

    def __str__(self):
        return "BO Base."

    def __repr__(self):
        return self.__str__()

    def get_model(self):
        return self.model

    def save_model(self):
        with self.session.begin():
            self.session.add(self.model)

    def merge_model(self, model):
        with self.session.begin():
            self.session.merge(model)

    def add_model(self, model):
        with self.session.begin(subtransactions=True):
            self.session.add(model)

    def merge_model_no_trans(self, model):
        self.session.merge(model)

    def execute_sql(self, sql):
        """
        execute sql
        """
        if not sql:
            return None
        q = self.session.execute(sql)
        return q


