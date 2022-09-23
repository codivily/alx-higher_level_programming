#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authentization': 'Basic ' + '{}:{}'.format(username, password)}
    headers['Accept'] = 'application/json'
    r = requests.post(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        print(data.get('id'))
    else:
        print(None)
