# -*- coding: utf-8 -*-
from scrapy.utils.request import request_fingerprint
from scrapy.http import Request

url = 'https://www.blueflags.cn?k1=123&k2=456'
req = Request(url=url)  # 用Request做封装
url2 = 'https://www.blueflags.cn?k1=456&k2=123'
req2 = Request(url=url)
fd = request_fingerprint(request=req)
fd2 = request_fingerprint(request=req2)
print(fd, fd2)
'''
c54f8702bcb7065bfb901f509fd6de6e60d93db2 c54f8702bcb7065bfb901f509fd6de6e60d93db2
'''
