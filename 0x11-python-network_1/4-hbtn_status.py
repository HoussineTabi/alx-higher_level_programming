#!/usr/bin/python3
"""
A python script taht fetches the url https://alx-intranet.hbtn.io/status.
"""
import requests
url = "https://alx-intranet.hbtn.io/status"


if __name__ == "__main__":
    resp = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(resp.text)))
    print('\t- content: {}'.format(resp.text))
