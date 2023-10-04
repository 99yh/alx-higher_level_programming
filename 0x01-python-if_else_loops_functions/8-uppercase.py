#!/usr/bin/python3
def uppercase(str):
    ret = ''
    for c in str:
        if 96 < ord(c) < 123:
            ret += chr(ord(c) - 32)
        else:
            ret += c
    print(ret)
