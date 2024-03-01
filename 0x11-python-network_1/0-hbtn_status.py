#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        infos = 'Body response:'\
                '\n\t- type: {}'\
                '\n\t- content: {}'\
                '\n\t- utf8 content: {}'
        print(infos.format(type(body), body, body.decode('utf8')))
