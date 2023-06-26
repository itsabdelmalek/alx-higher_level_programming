#!/usr/bin/python3

def safe_print_integer(value):
    # pycodestyle will check for code style conformity

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
