#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    i = 1
    if n:
        print(f'{n:d} argument{"s:" if n > 1 else ":"}')
    while i <= n:
        print(f"{i}: {sys.argv[i]}")
        i += 1
