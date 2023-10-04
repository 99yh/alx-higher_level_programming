#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        s = ''
        if not n % 3:
            s += 'Fizz'
        if not n % 5:
            s += 'Buzz'
        if s:
            print(s, end=' ')
        else:
            print(n, end=' ')
