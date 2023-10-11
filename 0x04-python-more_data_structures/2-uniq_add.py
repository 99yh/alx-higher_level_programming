#!/usr/bin/python3
def uniq_add(my_list=[]):
    if type(my_list) is list:
        return sum(set([i for i in my_list if type(i) is int]))
