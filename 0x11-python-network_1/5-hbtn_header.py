#!/usr/bin/python3
"""A script that takes in a URL, sends a request and display the value
in the X-Request-Id variable found in the header"""

if __name__ == '__main__':
    import sys
    import requests
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
