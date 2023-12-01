#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))
