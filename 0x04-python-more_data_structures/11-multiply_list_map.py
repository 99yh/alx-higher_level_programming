#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if type(my_list) is list and type(number) is int:
        return list(map(lambda x: x * number, my_list))
