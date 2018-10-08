# -*- coding: utf-8 -*-
# https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q=hello
import urllib
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host':'httpbin.org'
}

url = """https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q=hello"""
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
# page = urllib.urlopen(href, headers = headers)
print response.read()
