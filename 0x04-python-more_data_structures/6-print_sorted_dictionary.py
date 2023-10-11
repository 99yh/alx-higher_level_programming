#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) is dict:
        for k, v in sorted(a_dictionary.items()):
            print(f"{k}: {v}")
