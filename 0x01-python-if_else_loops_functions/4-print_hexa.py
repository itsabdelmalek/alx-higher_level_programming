#!/usr/bin/python3
for i in range(99):
    print("{:d} = 0x{:x}".format(i, i), end=' ' if i != 98 else '\n')
