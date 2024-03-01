#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    infos = 'Body response:'\
            '\n\t- type: {}'\
            '\n\t- content: {}'
    print(infos.format(type(res.text), res.text))
