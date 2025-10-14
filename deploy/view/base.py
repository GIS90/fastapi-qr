# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    base view

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/23 10:33"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:

design:
    - 参数在url中声明了，它将被解释为资源参数path
    - 参数是单一类型（例如int、float、str、bool等），它将被解释为查询参数query
    - 参数类型为继承Pydantic模块的BaseModel类的数据模型类，则它将被解释为请求体参数body

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python base.py
# ------------------------------------------------------------
from typing import List, Tuple, Dict, Set, Optional, Union
from fastapi import APIRouter, \
    Path, Query, \
    Body, Form, \
    Cookie, Header, \
    status as http_status, \
    HTTPException
from fastapi.responses import Response, \
    PlainTextResponse, JSONResponse, HTMLResponse, \
    StreamingResponse, FileResponse

from deploy.reqbody.base import UserBody as User
from deploy.utils.status import Status, SuccessStatus
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


# define view
base = APIRouter(prefix="", tags=["基础API：Path Query Body Form Cookie Header"])


@base.get('/',
          summary="Welcome to FastAPI-QR脚手架",
          description="Hello FastAPI-QR脚手架!",
          status_code=http_status.HTTP_200_OK
          )
async def hi() -> HTMLResponse:
    """
    :return: HTMLResponse
    """
    return HTMLResponse(
        content='''
            <h1 style="color:red">欢迎访问FastAPI-qr脚手架🚀🚀🚀🚀🚀🚀</h1>
            <hr>
            <h2>API文档说明请访问：<a href="/documentation/api/v1/docs">/documentation/api/v1/docs</a></h2>
            <h2>有问题请联系作者，邮箱：gaoming971366@163.com</h2>
            <hr>
            <h2 style="font-style: italic;color:blue">Enjoy the good life everyday！！!</h2>
        ''',
        status_code=http_status.HTTP_200_OK,
        headers={'X-Token': "I'm is test token............................................."}
    )


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Path
"""


@base.get('/user/{rtx_id}',
          summary="--必填--资源参数请求示例",
          description="必填资源参数请求"
          )
async def path_base(rtx_id: str) -> Status:
    """
    必填资源参数请求示例
    :param rtx_id: [str]资源请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/path-str/{rtx_id}',
          summary="**Path限制**字符型资源参数请求示例[非正则路径]",
          description="参数为字符型，使用fastapi.Path进行参数条件限制，包含description[描述]，min_length[最小长度]，max_length[最大长度]，regex[正则表达式]，参数限制可省略，"
                      "如果使用Path定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def path_str(
        rtx_id: str = Path(..., description="[字符型]资源参数rtx_id", min_length=1, max_length=12)
) -> Status:
    """
    Path限制字符型资源参数请求示例
    :param rtx_id: [str]资源请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/path-str-regex/{rtx_id}',
          summary="**Path限制**字符型资源参数请求示例[正则路径]",
          description="参数为字符型，使用fastapi.Path进行参数条件限制，包含description[描述]，min_length[最小长度]，max_length[最大长度]，regex[正则表达式]，参数限制可省略，"
                      "如果使用Path定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def path_str_regex(
        rtx_id: str = Path(..., description="[字符型]资源参数rtx_id", min_length=1, max_length=12, regex="user")
) -> Status:
    """
    Path限制字符型资源参数请求示例
    :param rtx_id: [str]资源请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/path-int/{rtx_id}',
          summary="**Path限制**整型资源参数请求示例",
          description="参数为整型，使用fastapi.Path进行参数条件限制，包含description[描述]，ge[大等于]，le[小等于]，gt[大于]，lt[小于]，参数限制可省略，"
                      "如果使用Path定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def path_int(
        rtx_id: int = Path(..., description="[整型]资源参数rtx_id", ge=1, le=10000)
) -> Status:
    """
    Path限制整型资源参数请求示例
    :param rtx_id: [int]资源请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Query
"""


@base.get('/user/query',
          summary="--必填--查询参数请求示例",
          description="必填查询参数请求"
          )
async def query_base(rtx_id: str) -> Status:
    """
    必填查询参数请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/query/null',
          summary="==非必填==查询参数请求示例",
          description="使用typing.Optional定义参数，参数值可为空值，在参数传递过程中设置默认值，为空可设置None"
          )
async def query_null(rtx_id: Optional[str] = None) -> Status:
    """
    非必填查询参数请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id or "default: qr"}
    )


@base.get('/user/query/q-str',
          summary="**Query限制**字符型查询参数请求示例[非正则参数请求]",
          description="参数为字符串，使用fastapi.Query进行参数条件限制，包含description[描述]，min_length[最小长度]，max_length[最大长度]，regex[正则表达式]，参数限制可省略，"
                      "如果使用Query定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def query_q_str(
        rtx_id: str = Query(..., description="查询参数rtx_id", min_length=1, max_length=12)
) -> Status:
    """
    Query限制字符型查询参数请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/query/q-str-regex',
          summary="**Query限制**字符型查询参数请求示例[正则参数请求]",
          description="参数为字符串，使用fastapi.Query进行参数条件限制，包含description[描述]，min_length[最小长度]，max_length[最大长度]，regex[正则表达式]，参数限制可省略，"
                      "如果使用Query定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def query_q_str_regex(
        rtx_id: str = Query(..., description="查询参数rtx_id", min_length=1, max_length=12, regex="user")
) -> Status:
    """
    Query限制字符型查询参数请求示例
    :param rtx_id: [str]查询请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )


@base.get('/user/query/q-int',
          summary="**Query限制**整型查询参数请求示例",
          description="参数为整型，使用fastapi.Query进行参数条件限制，包含description[描述]，ge[大等于]，le[小等于]，gt[大于]，lt[小于]，参数限制可省略，"
                      "如果使用Query定义参数为必填参数，第一个参数为...（看源码是语法糖写法）"
          )
async def query_q_int(
        rtx_id: int = Query(..., description="查询参数rtx_id", ge=1, le=10000)
) -> Status:
    """
    Query限制整型查询参数请求示例
    :param rtx_id: [int]查询请求参数
    :return: json
    """
    return SuccessStatus(
        data={'rtx_id': rtx_id}
    )

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Body
参数可以定义多个model：
    name: str,
    user01: User,
    user02: User,
    age: int,
    page: int = Query()
"""


@base.post("/request_body/user",
           summary="Pydantic模型请求体请求示例",
           description="参数类型为继承Pydantic模块的BaseModel类的数据模型类，则它将被解释为请求体参数body，Pydantic对于模型的属性字段采用Field类，Field具体相关使用请查询源码"
           )
def body(
        user: User
) -> Status:
    """
    Pydantic模型请求体请求示例
    :param user: User Pydantic模型
    :return: json

    dict()在新版本过时
    """
    return SuccessStatus(
        data=user.model_dump()
    )


@base.post("/request_body/user/{rtx_id}",
           summary="**Request Body + Path parameters + Query parameters**多参数",
           description="Pydantic定义Request Body，fastapi.Path定义资源请求参数，fastapi.Query定义查询请求参数，运用多参数的一个API示例"
           )
def body_request_body(
        rtx_id: str = Path(..., description="资源参数rtx_id", min_length=1, max_length=12, regex="user"),
        work_year: int = Query(..., description="查询参数work_year", ge=1, le=100),
        work_city: str = Query(..., description="资源参数work_city", min_length=1, max_length=12),
        user: Optional[User] = None
) -> Status:
    """
    :param rtx_id: [str]资源参数rtx_id
    :param work_year: [int]查询参数work_year
    :param work_city: [str]资源参数work_city
    :param user: [User]Pydantic模型，请求体参数
    :return: json

    dict()在新版本过时
    """
    return SuccessStatus(
        data={"rtx_id": rtx_id, "work_year": work_year, "work_city": work_city, "user": user.model_dump()}
    )


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Form
"""


@base.post("/form",
           summary="Form表单参数请求示例",
           description="定义Form表单请求参数，需要安装python-multipart包才支持Form表单验证, Form的使用与Path、Query差不多，具体查看源码"
           )
def form(
        username: str = Form(..., min_length=1, max_length=12, description="Form表单参数username"),
        password: str = Form(..., min_length=1, max_length=12, description="Form表单参数password")
) -> Status:
    """
    Cookie参数请求示例
    :param username: [str]Form表单参数username
    :param password: [str]Form表单参数password
    :return: json
    """
    return SuccessStatus(
        data={'username': username, 'password': password}
    )


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Cookie
"""


@base.get("/cookie",
          summary="Cookie参数请求示例",
          description="定义Cookie参数需要使用Cookie类，否则就是查询参数，测试请求只能用Postman（测试方案：Headers{Cookie: cookie=123abc}），并且Cookie的类属性与Path、Query差不多，这里使用Cookie参数为可选参数"
          )
def cookie(
        cookie_id: Optional[str] = Cookie(None, description="Cookie参数")
) -> Status:
    """
    Cookie参数请求示例
    :param cookie_id: [str]Cookie请求参数
    :return: json
    """
    return SuccessStatus(
        data={'cookie_id': cookie_id}
    )


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
Header
"""


@base.get("/header",
          summary="Header参数请求示例",
          description="Header同Path、Query、Cookie属性，包含字符串、整型相关的限制，具体操作请查看Header源码"
          )
def header(
        user_agent: Optional[str] = Header(None, convert_underscores=True, description="User-Agent"),
        x_token: str = Header(..., min_length=1, max_length=25, convert_underscores=True, description="X-Token")
) -> Status:
    """
    Header参数请求示例
    有些HTTP代理和服务器是不允许在请求头中带有下划线的，Header提供convert_underscores属性进行设置
    例如： convert_underscores=True会把user_agent变成user-agent
    :param user_agent: [str]Header参数user_agent
    :param x_token: [str]Header参数x_token
    :return: json
    """
    return SuccessStatus(
        data={"User-Agent": user_agent, "X-Token": x_token}
    )

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
deprecated
"""


@base.get('/deprecated',
          summary="过时接口示例",
          description="使用deprecated=True设置API过时，但是请求依然可以用",
          status_code=http_status.HTTP_200_OK,
          deprecated=True
          )
async def deprecated() -> Status:
    """
    :return: json
    """
    return SuccessStatus()

# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
