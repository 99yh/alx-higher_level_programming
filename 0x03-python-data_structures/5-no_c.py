#!/usr/bin/python3
def no_c(my_string):
    no_cC = ""
    for c in my_string:
        if c not in "cC":
            no_cC += c
    return no_cC
