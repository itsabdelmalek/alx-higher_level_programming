#!/usr/bin/python3

"""
This program prints the result of the addition of all arguments.
"""

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = sum(int(arg) for arg in args)
    print(total)
