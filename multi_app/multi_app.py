# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

'''
app01与app02使用不同的数据库
'''
app01 = Flask('app01')
app01.config['DB'] = 123
app02 = Flask('app02')
app02.config['DB'] = 456


@app01.route('/index')
def index():
    print('index')
    return 'index'


@app01.route('/login')
def login():
    print('login')
    return 'login'


@app02.route('/admin')
def amdin():
    print('admin')
    return 'admin'


@app02.route('/article')
def article():
    print('article')
    return 'article'


'''
/index
/login
/app02/admin
/app02/article
'''
app = DispatcherMiddleware(app01, {
    '/app02': app02
})
if __name__ == '__main__':
    run_simple(hostname='localhost', port=5000, application=app)
