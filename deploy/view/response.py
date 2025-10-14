# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    response view

    一、media-type是什么
        1、media-type是指媒体类型，它是一种在互联网上传输文件的标准化方式。一个文件可以通过media-type定义的方式告诉接收方它所属的类型。media-type在HTTP通信协议中的作用非常重要，它是HTTP协议通过ContentType字段传递给浏览器告诉浏览器如何解析资源的关键。
        2、media-type由type和subtype组成，中间用“/”隔开，例如text/html、image/jpeg、application/json等等。type表示文件的大类，比如text表示文本、image表示图像，application表示应用程序；subtype表示type下的具体类型，比如text类型下的subtype可以是plain、html、css等等。
        3、media-type指定的文件类型是一个通过标准化方式定义的概念，它帮助应用程序区分数据类型并按照类型进行处理，使得在数据传输和共享领域中使用不同的文件格式和处理方式成为可能。

        MediaType对象包含了三种信息：type 、subtype、charset，一般将这些信息传入parse()方法中，这样就可以解析出MediaType对象
        text/x-markdown; charset=utf-8

    二、media-type的种类
        text/html：HTML格式
        text/plain：纯文本格式，空格转换为 “+” 加号，但不对特殊字符编码
        text/xml：XML格式
        text/x-markdown：Markdown格式
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        image/gif：gif图片格式
        image/jpeg：jpg图片格式
        image/png：png图片格式
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        application/xhtml+xml：XHTML格式
        application/xml：XML数据格式
        application/json：用来告诉服务端，消息主体是序列化后的JSON字符串
        application/pdf：pdf格式
        application/msword：Word文档格式
        application/octet-stream：二进制流数据（如常见的文件下载）
        application/x-www-form-urlencoded：参数为键值对形式，在发送前编码所有字符（默认）。
            浏览器的原生 <form encType=”” 表单提交类型，如果不设置 enctype 属性，
            那么最终就会以 application/x-www-form-urlencoded 方式提交数据
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        multipart/form-data：Form表单字符编码，发送大量二进制数据或包含non-ASCII字符的文本,
            application/x-www-form-urlencoded是效率低下的（需要用更多字符表示一个non-ASCII字符）。
            需要设定“ <form enctype=‘multipart/form-data’”

    三、media-type的使用
        在Header中设置Content-Type: text/html; charset=UTF-8

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/26 16:43"
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
# usage: /usr/bin/python response.py
# ------------------------------------------------------------
from fastapi import APIRouter, status as http_status
from fastapi.responses import Response, \
    PlainTextResponse, HTMLResponse, \
    JSONResponse, StreamingResponse, RedirectResponse

from deploy.utils.enums import MediaType
from deploy.utils.status import Status, SuccessStatus, FailureStatus
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code
from deploy.reqbody.response import UserIn, UserOut


# define view
response = APIRouter(prefix="/response", tags=["Response对象类返回测试示例"])

headers = {"Hello": "World"}


# - - - - - - - - - - - - - - - - - - - - - - - - [Response返回类] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
@response.get("/response",
              summary="[Response返回类]Response对象测试用例",
              description="Response对象为基类，包含：content: typing.Any内容；status_code: int状态码，默认200；headers: Optional[typing.Mapping[str, str]]Header；media_type: Optional[str]媒体类型；background: Optional[BackgroundTask]后台任务")
async def base_response() -> Response:
    """
    :return: Response
    """
    """ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
    content: typing.Any内容,
    status_code: int状态码，默认200,
    headers: Optional[typing.Mapping[str, str]]Header,
    media_type: Optional[str]媒体类型,
    background: Optional[BackgroundTask]后台任务
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + """
    headers.update({"type": "Response"})
    return Response(
        content="I'm Response",
        status_code=http_status.HTTP_200_OK,
        headers=headers
    )


@response.get("/plaintext-response",
              summary="[Response返回类]PlainTextResponse对象测试用例",
              description="继承Response，media_type = text/plain，content直接展示字符串格式")
async def plaintext_response() -> PlainTextResponse:
    """
    :return: PlainTextResponse
    """
    """ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +    
    class PlainTextResponse(Response):
        media_type = "text/plain"
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + """
    headers.update({"type": "PlainTextResponse"})
    return PlainTextResponse(
        content="I'm PlainTextResponse",
        status_code=http_status.HTTP_200_OK,
        headers=headers,
        media_type=MediaType.TextPlain.value
    )


@response.get("/html-response",
              summary="[Response返回类]HTMLResponse对象测试用例",
              description="继承Response，media_type = text/html，content为HTML代码，直接编写HTML、CSS样式")
async def html_response() -> HTMLResponse:
    """
    :return: HTMLResponse
    """
    """ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +    
    class HTMLResponse(Response):
        media_type = "text/html"
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + """
    headers.update({"type": "HTMLResponse"})
    return HTMLResponse(
        content='''<h1 style="color:red">I'm HTMLResponse</h1>''',
        status_code=http_status.HTTP_200_OK,
        headers=headers,
        media_type=MediaType.TextHtml.value
    )


@response.get("/json-response",
              summary="[Response返回类]JSONResponse对象测试用例",
              description="继承Response，media_type = application/json，content为json数据")
async def json_response() -> JSONResponse:
    """
    :return: JSONResponse
    """
    """ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +    
    class JSONResponse(Response):
        media_type = "application/json"
    + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + """
    headers.update({"type": "JSONResponse"})
    content = Status(
        100, "I'm JSONResponse", {"k1": "v1", "k2": "v2", "k3": "v3"}
    ).status_body
    return JSONResponse(
        content=content,
        status_code=http_status.HTTP_200_OK,
        headers=headers,
        media_type=MediaType.APPJson.value
    )


# - - - - - - - - - - - - - - - - - - - - - - - - [Response返回参数]- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
@response.post("/response-model",
               response_model=UserOut,
               summary="[Response返回参数]response-model类测试用例",
               description="用指定的response-model来返回JSON值，通过response-model来优化不需要显示的字段")
async def response_model(user: UserIn):
    """
    :return: JSON
    """
    return user


data = {
    "d1": {"username": "法外狂徒张一", "password": "123456", "email": "gaoming@example.com", "phone": "123456789000", "full_name": "法外狂徒张三"},
    "d2": {"username": "法外狂徒张二", "password": "123456", "email": "gaoming@example.com", "phone": "123456789000", "full_name": "法外狂徒张三"},
    "d3": {"username": "法外狂徒张三", "password": "123456", "email": "gaoming@example.com", "phone": "123456789000", "full_name": "法外狂徒张三"},
    "d4": {"username": "法外狂徒张四", "password": "123456", "email": "gaoming@example.com", "phone": "123456789000", "full_name": "法外狂徒张三"},
}


@response.post("/response-model-include/{data_id}",
               response_model=UserIn,
               response_model_include={'username', 'password'},
               summary="[Response返回参数]response_model_include返回数据字段操作测试用例",
               description="response_model_include指定return json需要返回的字段列表，采用字典包含字段格式，例如：{'username', 'password'}，data_id数据包含：d1，d2，d3，d4。")
async def response_model_include(data_id: str):
    """
    :return: JSON
    """
    return data.get(data_id) or {"username": "无此用户"}


@response.post("/response-model-exclude/{data_id}",
               response_model=UserIn,
               response_model_exclude={'password', 'email'},
               summary="[Response返回参数]response_model_exclude返回数据字段操作测试用例",
               description="response-model-exclude指定return json需要过滤的字段列表，采用字典包含字段格式，例如：{'password', 'email'}，data_id数据包含：d1，d2，d3，d4。")
async def response_model_exclude(data_id: str):
    """
    :return: JSON
    """
    return data.get(data_id) or {"username": "无此用户"}


# * * * * * * * * * * * * * * * * * * * * * * * * * * [ END ] * * * * * * * * * * * * * * * * * * * * * * * * * * *
