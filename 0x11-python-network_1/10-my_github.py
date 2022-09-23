#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""

if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    r = requests.post(url, auth=HTTPBasicAuth(username, password))

    if r.status_code == 200:
        data = r.json()
        print(data.get('id'))
    else:
        print(None)
