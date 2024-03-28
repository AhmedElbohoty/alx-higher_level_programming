#!/usr/bin/python3
''' Python script that fetches https://alx-intranet.hbtn.io/status '''
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    respType = type(response.text)
    text = response.text

    print("Body response:")
    print(f"\t- type: {respType}")
    print(f"\t- content: {text}")
