#!/usr/bin/python3
"""
Python script taht fetches the url https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request
    with request.urlopen(url) as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
