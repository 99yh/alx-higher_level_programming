#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
