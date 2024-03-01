#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests


if __name__ == '__main__':
    res = requests.get(argv[1])
    if res.ok:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
