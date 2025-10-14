# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    app enter

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 21:36"
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
# usage: /usr/bin/python app.py
# ------------------------------------------------------------
import uvicorn
from deploy import create_app


# supervisor>uvicorn startup(PROD)
app = create_app()


"""========================================================================================="""
# manual startup(DEV)
if __name__ == "__main__":
    config = uvicorn.Config("app:app", port=22222, log_level="debug", reload=True)
    server = uvicorn.Server(config)
    server.run()
"""========================================================================================="""

