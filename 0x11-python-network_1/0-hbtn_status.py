#!/usr/bin/python3
''' Python script that fetches https://alx-intranet.hbtn.io/statu '''
import urllib.request

URL = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(URL) as response:
    html = response.read()

content = html.decode("utf-8")

print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content: {}".format(content))
