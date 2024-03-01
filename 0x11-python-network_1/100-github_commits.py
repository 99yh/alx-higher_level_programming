#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    params = {'per_page': 10}
    res = requests.get(url, params=params)
    all = res.json()
    for commit in res.json():
        sha = commit.get('sha')
        author = dict(commit.get('author')).get('name')
        print(f'{sha}: {author}')
