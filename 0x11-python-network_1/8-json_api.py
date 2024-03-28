#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

url = "http://0.0.0.0:5000/search_user"

if __name__ == "__main__":
    argv = sys.argv

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    data = {"q": q}
    response = requests.post(url, data=data)
    try:
        respJSON = response.json()
        id = respJSON.get("id")
        name = respJSON.get("name")
        if len(respJSON) == 0 or not id or not name:
            print("No result")
        else:
            print(f"[{id}] {name}")
    except Exception:
        print("Not a valid JSON")
