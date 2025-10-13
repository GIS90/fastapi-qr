# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    config

base_info:
    __author__ = "PyGo"
    __time__ = "2023/11/22 21:41"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:

design:
    2024.10.08 update：采用pathlib方式

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python config.py
# ------------------------------------------------------------
import os
import sys
import yaml
import logging
from pathlib import Path


# config file absolute path
config_abspath_file = Path(__file__).resolve()
if not config_abspath_file.is_absolute():
    _os_path = os.path.dirname(os.path.abspath(__file__))
    config_abspath_file = Path(_os_path)
# logging.basicConfig()
logger = logging.getLogger(__name__)


# get deploy folder, solve is or not frozen of the script
def _get_deploy_folder():
    return config_abspath_file.parent


# get deploy folder, solve is or not frozen of the script
def _get_root_folder():
    return _get_deploy_folder().parent


# get current run config by mode
def _get_config(mode='dev'):
    # not allow mode parameters
    if mode not in ['dev', 'prod']:
        return None
    # root path is not abs
    root = _get_root_folder()
    if not root.is_absolute():
        return None
    
    return root.joinpath('etc').joinpath(mode).joinpath('config.yaml')


# default log dir
def _get_log_folder():
    root = _get_root_folder()
    if not root.is_absolute():
        return None

    return root.joinpath('log')


"""
default config
avoid initialization parameters is empty
"""
# SERVER
NAME = 'Quick-Run API'
VERSION = 'v1.0.1'
DEBUG = True
ADMIN = 'admin'
ADMIN_AUTH_LIST = []

# APP > 中间件
APP_SECRET_KEY = "IbelivemeIcanfly-gaomingliang"
APP_ALLOW_HOSTS = []  # IP列表 ["127.0.0.1"]
APP_CORS_ORIGINS = ["*"]
APP_SESSION_MAX_AGE = 15 * 24 * 60 * 60  # unit: minute, default 15 days
APP_BAN_ROUTERS = ['/ban1', '/ban2']
APP_M_GZIP_SIZE = 1000
APP_M_GZIP_LEVEL = 9
APP_M_ALLOW_HOSTS = []  # TrustedHostMiddleware，支持ip、domain
APP_REQUEST_METHODS = ["GET", "POST", "PUT", "DELETE"]  # 允许通过的请求方法列表
# APP > Docs文档配置
APP_OPENAPI_URL = "/openapi.json"
APP_DOCS_URL = "/docs"
APP_REDOC_URL = "/redoc"
# APP > 静态资源
APP_STATIC_URL = "/static"
APP_STATIC_DIR = "static"

# DB(sqlalchemy)，default is mysql
DB_LINK = None

# Redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = None

# LOG
LOG_DIR = _get_log_folder()
LOG_LEVEL = "debug"
LOG_FORMATTER = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s - %(message)s"
LOG_FILENAME_PREFIX = 'base_webframe'

# mail
MAIL_SERVER = None
MAIL_PORT = None
MAIL_USE_SSL = None
MAIL_USERNAME = None
MAIL_PASSWORD = None

# jwt token
JWT_TOKEN_SECRET_KEY = "Enjoy the good life everyday！！!"  # 密钥
JWT_TOKEN_ALGORITHM = "HS256"  # 算法
JWT_TOKEN_EXPIRE_MINUTES = 60 * 4   # 访问令牌过期时间，单位：分


# others
NON = 'NoNameBody'

"""
Entry: initialize config
"""
mode = os.environ.get('mode') or 'dev'
_config_file = _get_config(mode)
if not os.path.exists(_config_file):
    logger.critical('====== config file is not exist, exit ======')
    sys.exit(1)

with open(_config_file, 'r', encoding='UTF-8') as f:
    _config_info = yaml.safe_load(f)
    if not _config_info:
        logger.critical('====== config file is unavail, exit ======')
        sys.exit(1)

    # SERVER
    SERVER_NAME = _config_info['SERVER']['NAME'] or NAME
    SERVER_VERSION = _config_info['SERVER']['VERSION'] or VERSION
    SERVER_DEBUG = _config_info['SERVER']['DEBUG'] or DEBUG
    SERVER_ADMIN = _config_info['SERVER']['ADMIN'] or ADMIN
    SERVER_ADMIN_AUTH_LIST = _config_info['SERVER']['ADMIN_AUTH_LIST'] or ADMIN_AUTH_LIST

    # APP > 中间件
    APP_SECRET_KEY = _config_info['APP']['SECRET_KEY'] or APP_SECRET_KEY
    APP_ALLOW_HOSTS = _config_info['APP']['ALLOW_HOSTS'] or APP_ALLOW_HOSTS
    APP_CORS_ORIGINS = _config_info['APP']['CORS_ORIGINS'] or APP_CORS_ORIGINS
    APP_SESSION_MAX_AGE = _config_info['APP']['SESSION_MAX_AGE'] or APP_SESSION_MAX_AGE
    APP_BAN_ROUTERS = _config_info['APP']['BAN_ROUTERS'] or APP_BAN_ROUTERS
    APP_M_GZIP_SIZE = _config_info['APP']['M_GZIP_SIZE'] or APP_M_GZIP_SIZE
    APP_M_GZIP_LEVEL = _config_info['APP']['M_GZIP_LEVEL'] or APP_M_GZIP_LEVEL
    APP_M_ALLOW_HOSTS = _config_info['APP']['M_ALLOW_HOSTS'] or APP_M_ALLOW_HOSTS
    APP_REQUEST_METHODS = _config_info['APP']['REQUEST_METHODS'] or APP_REQUEST_METHODS
    # APP > docs
    APP_OPENAPI_URL = _config_info['APP']['OPENAPI_URL'] or APP_OPENAPI_URL
    APP_DOCS_URL = _config_info['APP']['DOCS_URL'] or APP_DOCS_URL
    APP_REDOC_URL = _config_info['APP']['REDOC_URL'] or APP_REDOC_URL
    # APP > 静态资源
    APP_STATIC_URL = _config_info['APP']['STATIC_URL'] or APP_STATIC_URL
    APP_STATIC_DIR = _config_info['APP']['STATIC_DIR'] or APP_STATIC_DIR
    APP_STATIC_ABS_DIR = os.path.join(_get_deploy_folder(), APP_STATIC_DIR)
    if not os.path.exists(APP_STATIC_ABS_DIR):
        os.makedirs(APP_STATIC_ABS_DIR)

    # DB(sqlalchemy)，default is mysql
    DB_LINK = _config_info['DB']['DB_LINK'] or DB_LINK

    # Redis
    REDIS_HOST = _config_info['REDIS']['HOST'] or REDIS_HOST
    REDIS_PORT = _config_info['REDIS']['PORT'] or REDIS_PORT
    REDIS_DB = _config_info['REDIS']['DB'] or REDIS_DB
    REDIS_PASSWORD = _config_info['REDIS']['PASSWORD'] or REDIS_PASSWORD

    # LOG
    if _config_info['LOG']['LOG_DIR']:
        LOG_DIR = os.path.join(os.path.dirname(_get_deploy_folder()), _config_info['LOG']['LOG_DIR'])
    else:
        LOG_DIR = LOG_DIR
    if not os.path.exists(LOG_DIR):
        logger.critical('====== log dir is not exist, create %s... ======' % LOG_DIR)
        os.makedirs(LOG_DIR)
    LOG_LEVEL = _config_info['LOG']['LOG_LEVEL'] or LOG_LEVEL
    LOG_FORMATTER = _config_info['LOG']['LOG_FORMATTER'] or LOG_FORMATTER
    LOG_FILENAME_PREFIX = _config_info['LOG']['LOG_FILENAME_PREFIX'] or LOG_FILENAME_PREFIX

    # MAIL
    MAIL_SERVER = _config_info['MAIL']['MAIL_SERVER'] or MAIL_SERVER
    MAIL_PORT = int(_config_info['MAIL']['MAIL_PORT']) or MAIL_PORT
    MAIL_USE_SSL = _config_info['MAIL']['MAIL_USE_SSL'] or MAIL_USE_SSL
    MAIL_USERNAME = _config_info['MAIL']['MAIL_USERNAME'] or MAIL_USERNAME
    MAIL_PASSWORD = _config_info['MAIL']['MAIL_PASSWORD'] or MAIL_PASSWORD

    # JWT
    JWT_TOKEN_SECRET_KEY = _config_info['JWT']['SECRET_KEY'] or JWT_TOKEN_SECRET_KEY
    JWT_TOKEN_ALGORITHM = _config_info['JWT']['ALGORITHM'] or JWT_TOKEN_ALGORITHM
    JWT_TOKEN_EXPIRE_MINUTES = int(_config_info['JWT']['EXPIRE_MINUTES']) or JWT_TOKEN_EXPIRE_MINUTES

    # OTHERS
    O_NON = _config_info['OTHERS']['NON'] or NON
