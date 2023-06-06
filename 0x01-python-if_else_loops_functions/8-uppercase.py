#!/usr/bin/python3

def uppercase(string):
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
