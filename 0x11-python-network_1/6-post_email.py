#!/usr/bin/python3
"""
A python script that takes in url and an eamil address
and sends a POST request to the passed url
"""
import requests
from sys import argv


if __name__ == "__name__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print("{}".format(r.text))
