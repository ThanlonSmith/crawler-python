# -*- coding: utf-8 -*-
from multi_app import app01, app02

with app01.app_context():
    pass  # 为app01创建数据库
    with app02.app_context():
        pass  # 为app02创建数据库
