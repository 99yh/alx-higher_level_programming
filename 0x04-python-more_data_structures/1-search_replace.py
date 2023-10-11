#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if type(my_list) is not list:
        return None
    return [(elem if elem != search else replace) for elem in my_list]
