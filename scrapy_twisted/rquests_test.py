# -*- coding: utf-8 -*-
import requests

url_request = ['https://www.blueflags.cn/', 'https://segmentfault.com/', 'https://stackoverflow.com/']
for item in url_request:
    '''
    一个一个串行地等待
    '''
    response = requests.get(item)
    print(response.text)