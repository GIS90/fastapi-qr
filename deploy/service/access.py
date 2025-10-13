# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    access service

base_info:
    __author__ = "PyGo"
    __time__ = "2024/11/20 22:41"
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
# usage: /usr/bin/python access.py
# ------------------------------------------------------------
from deploy.bo.sysuser import SysUserBo
from deploy.utils.utils import d2s, get_now


USER_DEFAULT_AVATAR = ""


class AccessService(object):
    """
    Access Service
    """
    base_attrs = ['id', 'rtx_id', 'md5_id', 'fullname', 'password',
                  'email', 'phone', 'avatar', 'introduction',
                  'department', 'role', 'is_del']

    extend_attrs = ['create_time', 'create_rtx', 'delete_time', 'delete_rtx']

    update_attrs = ['name', 'email', 'phone', 'introduction']

    password_attrs = ['old_password', 'new_password', 'con_password']

    def __init__(self):
        """
        ApiService class initialize
        """
        super(AccessService, self).__init__()
        # bo
        self.sysuser_bo = SysUserBo()

    def __str__(self):
        print("AccessService class.")

    def __repr__(self):
        self.__str__()

    def _model_to_dict(self, model, _type: str = 'base') -> dict:
        """
        user model transfer to dict data
        model: user model

        format user object
        """
        if not model:
            return {}
        if _type == 'base':
            attrs = self.base_attrs
        elif _type == 'all':
            attrs = self.base_attrs + self.extend_attrs
        else:
            attrs = self.base_attrs
        _res = dict()
        for attr in attrs:
            if attr == 'id':
                _res[attr] = model.id
            elif attr == 'rtx_id':
                _res[attr] = model.rtx_id
            elif attr == 'md5_id':
                _res[attr] = model.md5_id
            elif attr == 'fullname':
                _res['name'] = model.fullname
            elif attr == 'password':
                _res[attr] = model.password
            elif attr == 'email':
                _res[attr] = model.email or ""
            elif attr == 'phone':
                _res[attr] = model.phone or ""
            elif attr == 'avatar':
                _res[attr] = model.avatar or USER_DEFAULT_AVATAR
            elif attr == 'introduction':
                _res[attr] = model.introduction or ""
            elif attr == 'department':
                _res[attr] = model.department or ""
            elif attr == 'role':    # 多角色，存储role的engname，也就是role的rtx_id
                _res[attr] = str(model.role).split(';') if model.role else []
            elif attr == 'create_time':
                _res[attr] = d2s(model.create_time) \
                    if not isinstance(model.create_time, str) else model.create_time or ''
            elif attr == 'create_rtx':
                _res[attr] = model.create_rtx or ''
            elif attr == 'is_del':
                _res[attr] = True if model.is_del else False
            elif attr == 'delete_time':
                _res[attr] = d2s(model.delete_time) \
                    if not isinstance(model.delete_time, str) else model.delete_time or ''
            elif attr == 'delete_rtx':
                _res[attr] = model.delete_rtx or ""
        else:
            return _res

    def open2lisapi_login_rtx(self, rtx_id: str) -> dict:
        user_res = dict()
        if not rtx_id:
            return user_res

        user = self.sysuser_bo.get_login_by_params(rtx_id)  # 用户多参登录方法
        return self._model_to_dict(user, _type='base') if user else user_res


