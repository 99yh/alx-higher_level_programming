#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/users/' + argv[1]
    res = requests.get(url)
    print(res.json().get('id'))
