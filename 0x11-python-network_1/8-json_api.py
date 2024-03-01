#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': argv[1] if len(argv) > 1 else ''}
    res = requests.get(url, params=params)
    try:
        json = res.json()
        if (json):
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
