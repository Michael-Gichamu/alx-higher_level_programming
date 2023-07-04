#!/usr/bin/python3
"""
Takes Github credentials(username and password) and
uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(None)
