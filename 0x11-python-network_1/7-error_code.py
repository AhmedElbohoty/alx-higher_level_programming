#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL
and displays the body of the response. '''
import sys
import requests

if __name__ == '__main__':
    argv = sys.argv
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        code = response.status_code
        print(f"Error code: {code}")
    else:
        print(response.text)
