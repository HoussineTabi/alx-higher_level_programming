#!/usr/bin/python3
"""
A python script that takes in url and an eamil address
and sends a POST request to the passed url
"""
import requests
from sys import argv


if __name__ == "__name__":
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    resp = requests.post(url, data=payload)
