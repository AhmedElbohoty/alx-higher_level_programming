#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


url = "https://api.github.com/user"


def my_github(username, password):
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        user_id = data["id"]
        print(user_id)
    else:
        print(None)


if __name__ == "__main__":
    argv = sys.argv
    my_github(argv[1], argv[2])
