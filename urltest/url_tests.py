import requests

'''
r = requests.get('http://oorraa.ru/')
print(r.status_code)
'''

# -*- coding:utf-8 -*-
import requests
resp = requests.get('http://oorraa.com')
print resp.status_code
print resp.headers
print resp.text