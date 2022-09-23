#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    print('Body response:')
    print('    - type: {}'.format(type(response)))
    print('    - content: {}'.format(body))
    print('    - utf8 content: {}'.format(body.decode('utf-8')))
