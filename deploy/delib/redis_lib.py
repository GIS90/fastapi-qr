# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 
    redis lib

base_info:
    __author__ = "PyGo"
    __time__ = "2024/12/12 21:20"
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
# usage: /usr/bin/python redis_lib.py
# ------------------------------------------------------------
from typing import Optional
import redis
from contextlib import contextmanager

from deploy.config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD


class RedisClientLib(object):
    def __init__(self, host: str, port: int, db: int, password: Optional[str], decode_responses=True):
        self.HOST = host
        self.PORT = port
        self.DB = db
        self.PASSWORD = password
        self.decode_responses = decode_responses
        self._connection = None

    def __str__(self):
        return "RedisClientLib Class "

    def __repr__(self):
        return self.__str__()

    @property
    def connection(self):
        if not self._connection:
            try:
                self._connection = redis.StrictRedis(
                    host=self.HOST,
                    port=self.PORT,
                    db=self.DB,
                    password=self.PASSWORD,
                    decode_responses=self.decode_responses
                )
            except redis.RedisError as e:
                print(f"RedisClientLib create connect failed: {e}")

        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    @contextmanager
    def get_connection(self):
        try:
            yield self.connection
        finally:
            # 如果需要，可以在这里进行清理工作，不过对于 Redis 连接通常不需要
            pass

    def set_key(self, key, value, ex=None, px=None, nx=False, xx=False):
        """Set the value at key ``name`` to ``value``"""
        with self.get_connection() as conn:
            return conn.set(key, value, ex, px, nx, xx)

    def get_key(self, key):
        """Return the value at key ``name``, or None if the key doesn't exist"""
        with self.get_connection() as conn:
            return conn.get(key)

    def delete_key(self, *keys):
        """Delete one or more keys specified by ``keys``"""
        with self.get_connection() as conn:
            return conn.delete(*keys)

    def expire_key(self, key, time):
        """Set an expiration on key ``name``. ``time`` can be repr'd as an int."""
        with self.get_connection() as conn:
            return conn.expire(key, time)

    def ttl_key(self, key):
        """Returns the remaining time to live of a key that has a timeout"""
        with self.get_connection() as conn:
            return conn.ttl(key)


# 创建一个长久连接
redis_cli_long = RedisClientLib(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)
