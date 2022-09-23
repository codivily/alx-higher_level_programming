#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response (decoded
in utf-8)"""

if __name__ == '__main__':
    import sys
    import requests

    term = ""
    if len(sys.argv) > 1:
        term = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': term})

    try:
        data = r.json()
        if not data:
            print 'No result'
        else:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
