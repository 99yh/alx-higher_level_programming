#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
