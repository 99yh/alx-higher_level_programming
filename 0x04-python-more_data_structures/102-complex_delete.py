#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if type(a_dictionary) is dict:
        to_del = []
        for k, v in a_dictionary.items():
            if v == value:
                to_del.append(k)
        for k in to_del:
            del a_dictionary[k]

    return a_dictionary
