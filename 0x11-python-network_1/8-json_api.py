#!/usr/bin/python3
"""
A python script that takes in a letter and sends a psot request
To http://0.0.0.0:5000/search_user
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except ValueError:
        print("Not a valid JSON")
