#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    if type(a_dictionary) is dict:
        for k, v in a_dictionary.items():
            res[k] = v * 2
    return res
