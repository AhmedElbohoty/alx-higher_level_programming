#!/usr/bin/python3
'''Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response.'''
import sys
import requests

if __name__ == '__main__':
    argv = sys.argv
    url = argv[1]
    email = argv[2]

    payload = {'email': email}
    response = requests.post(argv[1], data=payload)

    print(response.text)
