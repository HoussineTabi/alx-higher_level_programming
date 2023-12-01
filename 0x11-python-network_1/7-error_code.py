#!/usr/bin/python3
"""
A python script that takes in a url and sends
a request to the url and displays the nody of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
