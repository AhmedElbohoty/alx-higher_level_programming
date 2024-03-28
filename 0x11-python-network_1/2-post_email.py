#!/usr/bin/python3
''' Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)'''
import urllib.request as request
import urllib.parse as parse
import sys

if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    email = argv[2]

    params = {'email': email}
    data = parse.urlencode(params).encode('utf-8')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
