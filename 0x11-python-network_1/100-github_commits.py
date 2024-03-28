#!/usr/bin/python3
"""Write a Python script that takes 2 arguments in order to solve challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)"""
import sys
import requests


def get_commits(repo, owner):
    ''' Get repo commits '''
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    commits = response.json()[:10]
    for commit in commits:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))


if __name__ == "__main__":
    argv = sys.argv
    get_commits(argv[1], argv[2])
