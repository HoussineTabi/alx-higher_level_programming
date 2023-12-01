#!/usr/bin/python3
"""
A python script that takes github user name and password
to display the id
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/usr'
    resp = requests.get(url, auth=(argv[1], argv[2]))
    resp_json = resp.json()
    if resp_json == {}:
        print("None")
    else:
        print("{}".fomat(resp_json.get['id']))
