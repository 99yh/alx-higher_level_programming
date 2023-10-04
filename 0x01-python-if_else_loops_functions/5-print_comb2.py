#!/usr/bin/python3
for n in range(100):
    print(f'{n:02d}', end=', ' if n < 99 else None)
