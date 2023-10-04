#!/usr/bin/python3
for n in range(8):
    for q in range(n + 1, 10):
        print(f'{n:d}{q:d}', end=', ')
print(f'{n + 1:d}{q:d}')
