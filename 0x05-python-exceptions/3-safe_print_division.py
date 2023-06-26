#!/usr/bin/python3

def safe_print_division(a, b):

    # pycodestyle will check for code style conformity

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
