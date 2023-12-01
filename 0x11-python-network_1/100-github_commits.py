#!/usr/bin/python3
"""
Lists the 10 most recent comments on the given github repository.
Usage: ./100-githuub_commits.py <repository name> <repository owner>
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    resp = requests.get(url)
    commits = resp.json()
    try:
        for count in range(10):
            print("{}: {}".format(
                commits[count].get("sha"),
                commits[count].get("commit").get("author").get("name")))
    except IndexError:
        pass
