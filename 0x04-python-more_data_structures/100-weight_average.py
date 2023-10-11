#!/usr/bin/python3
def weight_average(my_list=[]):
    if type(my_list) is not list or not my_list:
        return 0
    bast = 0
    mqam = 0
    for tup in my_list:
        tup = tup + (0, 0)
        bast += tup[0] * tup[1]
        mqam += tup[1]

    if mqam:
        return float(bast) / mqam
    return 0
