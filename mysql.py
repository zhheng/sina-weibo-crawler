#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
from wcrawler import *


# 数据库查询cookie

def get_cookies():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "mysql123", "weibo")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT cookie FROM auth")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()

    return [cookie[0] for cookie in data]

