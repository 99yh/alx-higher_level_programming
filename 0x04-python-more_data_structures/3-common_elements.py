#!/usr/bin/python3
def common_elements(set_1, set_2):
    if type(set_1) is type(set_2) is set:
        return set_1 & set_2
