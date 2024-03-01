#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as res:
    print(res.headers.get('X-Request-Id'))
