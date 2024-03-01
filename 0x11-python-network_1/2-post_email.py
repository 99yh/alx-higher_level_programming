#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
import urllib.request
import urllib.parse
import sys


data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as res:
    print(res.read().decode('utf8'))
