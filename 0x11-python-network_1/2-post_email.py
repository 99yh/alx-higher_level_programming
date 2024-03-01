#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from sys import argv


data = urlencode({'email': argv[2]}).encode('ascii')
print(data)
req = Request(argv[1], data)
with urlopen(req) as res:
    print(res.read().decode('utf8'))
