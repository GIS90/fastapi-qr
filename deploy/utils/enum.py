# -*- coding= utf-8 -*-

"""
------------------------------------------------

describe:
    enum

base_info=
    __author__ = "PyGo"
    __time__ = "2023/11/26 17=16"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "z2lisapi"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life every day！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage= /usr/bin/python enum.py
# ------------------------------------------------------------
from enum import Enum, unique


__all__ = [
    'MediaType',
]


@unique
class MediaType(Enum):
    """
    http协议数据类型
    """
    TextPlain = "text/plain"
    TextHtml = "text/html"
    TextXml = "text/xml"
    TextMarkDown = "text/x-markdown"

    ImageGif = "image/gif"
    ImageJpg = "image/jpg"
    ImagePng = "image/png"

    APPXHtml = "application/xhtml"
    APPXml = "application/xml"
    APPJson = "application/json"
    APPPdf = "application/pdf"
    APPWord = "application/msword"
    APPStream = "application/octet-stream"
    APPForm = "application/x-www-form-urlencoded"

    MulForm = "multipart/form-data"

