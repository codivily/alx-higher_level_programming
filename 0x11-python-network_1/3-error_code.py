#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response (decoded
in utf-8)"""

if __name__ == '__main__':
    import sys
    import urllib.error
    import urllib.request
    import urllib.parse

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
