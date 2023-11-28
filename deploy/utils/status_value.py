# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe:
    status value

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 22:33"
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
Life is short I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python status_msg.py
# ------------------------------------------------------------
from enum import Enum, unique


# Status status
@unique
class StatusEnum(Enum):
    SUCCESS = "success"
    FAILURE = "failure"


# Status message
StatusMsg = {
    # ** success **
    100: "成功",
    101: "成功，请求数据为空",

    # ** login **
    200: "用户未登录",
    201: "用户不存在",
    202: "用户未注册",
    203: "用户已注销",
    204: "输入的账户/密码有误",
    205: "用户TOKEN验证失败",
    206: "用户输入的旧密码有误",
    207: "输入的两次新密码不一致",

    # ** request method **
    300: "请求方式错误",

    # ** request parameter **
    400: "没有发现请求参数",
    4001: "缺少请求参数",
    4002: "缺少RTX-ID信息",
    401: "请求参数类型不合法",
    402: "请求参数不允许为空",
    403: "请求参数错误",
    # ** request file **
    450: "缺少上传文件",
    451: "文件不存在",
    452: "文件内容不存在",
    453: "文件超过最大65535行数",
    454: "文件格式不支持",
    455: "文件内容不符合要求",
    456: "文件本地存储失败",
    457: "文件云存储失败",
    458: "文件数据已存在",
    459: "文件导出数据为空",
    460: "文件全部上传失败",
    461: "文件部分上传失败",
    462: "文件存储数据库记录失败",
    463: "文件超出操作的SHEET索引",
    464: "文件存储目录不存在",
    465: "文件压缩有误",

    # ** data **
    500: "管理员用户，不允许操作",
    501: "数据不存在",
    502: "数据已存在，不允许新增",
    503: "数据已删除，不允许操作",
    504: "非数据权限人员，无权限操作",

    # ** db **
    600: "数据库异常",
    601: "数据库新增失败",
    602: "数据库删除失败",
    603: "数据库更新失败",
    604: "数据库提交失败",

    # ** other **
    900: "第三方API接口异常",
    901: "HTTP异常",
    999: "未知名异常",

    # ** 自定义异常原因 **
    10000: "自定义异常原因",

}


# Status code
@unique
class StatusCode(Enum):
    # ** success **
    CODE_100_SUCCESS = 100
    CODE_101_SUCCESS_NO_DATA = 101

    # ** login **
    CODE_200_LOGIN_NOT = 200
    CODE_201_LOGIN_USER_NOT_EXIST = 201
    CODE_202_LOGIN_USER_NO_REGISTER = 202
    CODE_203_LOGIN_USER_OFF = 203
    CODE_204_LOGIN_USER_PASSWORD_ERROR = 204
    CODE_205_TOKEN_VERIFY_FAILURE = 205
    CODE_206_USER_OLD_PASSWORD_ERROR = 206
    CODE_207_USER_NEW_PASSWORD_NOT_MATCH = 207

    # ** request method **
    CODE_300_REQUEST_METHOD_ERROR = 300

    # ** request parameter **
    CODE_400_REQUEST_PARAMETER_MISS = 400
    CODE_4001_REQUEST_PARAMETER_MISS_ONE = 4001
    CODE_4002_REQUEST_PARAMETER_MISS_RTX = 4002
    CODE_401_REQUEST_PARAMETER_TYPE_ILLEGAL = 401
    CODE_402_REQUEST_PARAMETER_NOT_NULL = 402
    CODE_403_REQUEST_PARAMETER_ERROR = 403
    # ** request file **
    CODE_450_REQUEST_FILE_NO_UPLOAD = 450
    CODE_451_REQUEST_FILE_NOT_EXIST = 451
    CODE_452_REQUEST_FILE_NOT_CONTENT = 452
    CODE_453_REQUEST_FILE_EXCEED_MAX_ROW = 453
    CODE_454_REQUEST_FILE_NOT_SUPPORT = 454
    CODE_455_REQUEST_FILE_CONTENT_ERROR = 455
    CODE_456_REQUEST_FILE_LOCAL_STORE_FAILURE = 456
    CODE_457_REQUEST_FILE_YUN_STORE_FAILURE = 457
    CODE_458_REQUEST_FILE_DATA_EXIST = 458
    CODE_459_REQUEST_FILE_EXPORT_NULL = 459
    CODE_460_REQUEST_FILES_UPLOAD_ALL_FAILURE = 460
    CODE_461_REQUEST_FILES_UPLOAD_PART_FAILRE = 461
    CODE_462_REQUEST_FILE_STORE_DB_FAILURE = 462
    CODE_463_REQUEST_FILE_EXCEED_SHEET_INDEX = 463
    CODE_464_REQUEST_FILE_STORE_FOLDER = 464
    CODE_465_REQUEST_FILE_COMPRESS_ERROR = 465

    # ** data **
    CODE_500_DATA_ADMIN_NOT = 500
    CODE_501_DATA_NOT_EXIST = 501
    CODE_502_DATA_EXIST_NOT_ADD = 502
    CODE_503_DATA_DELETE_NOT_EDIT = 503
    CODE_504_DARA_AUTH_NOT_EDIT = 504

    # ** db **
    CODE_600_DB_EXCEPTION = 600
    CODE_601_DB_ADD_FAILURE = 601
    CODE_602_DB_DELETE_FAILURE = 602
    CODE_603_DB_UPDATE_FAILURE = 603
    CODE_604_DB_COMMIT_FAILURE = 604

    # ** other **
    CODE_900_OTHER_THREE_API_EXCEPTION = 900
    CODE_901_HTTP_EXCEPTION = 901
    CODE_999_NO_KNOWN_EXCEPTION = 999

    # ** 自定义异常原因 **
    CODE_10000_EXCEPTION = 10000
