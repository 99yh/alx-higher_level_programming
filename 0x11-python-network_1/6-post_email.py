#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
import sys
import requests


if __name__ == '__main__':
    res = requests.post(sys.argv[1], params={'email': sys.argv[2]})
    print(res.text)
