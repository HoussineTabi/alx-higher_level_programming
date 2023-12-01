#!/usr/bin/python3
"""
A python script takes in a url and sends a request to the url and
Display value of the variable X-Response-Id.
"""
from sys import argv
import requests

if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.header.get('x-Response-Id'))
