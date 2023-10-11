#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if type(a_dictionary) is dict and key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
