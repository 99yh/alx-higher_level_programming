#!/usr/bin/python3
def max_integer(my_list=[]):
    x = None if not my_list else my_list[0]
    for i in my_list[1:]:
        if x < i:
            x = i

    return x
