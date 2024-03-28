#!/usr/bin/python3
"""Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)"""
import sys
import requests


def get_commits(repo, owner):
    ''' Get repo commits '''
    url = f'https://api.github.com/repos/{owner}/{repo}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        print("Repository details:")
        print("Name:", data['name'])
        print("Owner:", data['owner']['login'])
        print("Description:", data['description'])
        print("URL:", data['html_url'])
        print("Stars:", data['stargazers_count'])
        print("Watchers:", data['subscribers_count'])
        print("Forks:", data['forks_count'])


if __name__ == "__main__":
    argv = sys.argv
    get_commits(argv[1], argv[2])
