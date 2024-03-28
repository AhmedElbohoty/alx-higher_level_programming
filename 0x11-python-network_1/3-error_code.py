#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).Python script that takes in a URL,
sends a request to the URL and displays the body of the
response (decoded in utf-8)."""
import urllib.request as request
import urllib.error as error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
