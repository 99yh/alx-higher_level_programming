#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1
    i = 1
    result = 0
    while i <= n:
        result += int(argv[i])
        i += 1
    print(result)
