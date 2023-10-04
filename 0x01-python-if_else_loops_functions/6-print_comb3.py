#!/usr/bin/python3
for n in range(8):
    for q in range(n + 1, 10):
        print('{:d}{:d}'.format(n, q), end=', ')
print('{:d}{:d}'.format(n + 1, q))
