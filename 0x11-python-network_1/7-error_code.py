#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests


if __name__ == '__main__':
    try:
        res = requests.get(argv[1])
        print(res.text)
    except requests.HTTPError as e:
        print("Error code: {}".format(e.code))
