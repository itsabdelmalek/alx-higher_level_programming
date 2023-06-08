#!/usr/bin/python3

"""
This program prints the number of and the list of its arguments.
"""

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args))
    print("Argument{}:{}".format("s" if num_args != 1 else "", "" if num_args == 0 else " "))

    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
