#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from sys import argv
import requests

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    params = {'per_page': 10}
    res = requests.get(url, params=params)
    all = res.json()
    if type(all) is not list:
        all = []
    for commit in all:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f'{sha}: {author}')
