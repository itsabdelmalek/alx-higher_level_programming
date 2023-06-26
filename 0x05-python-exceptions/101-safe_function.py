#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    # pycodestyle will check for code style conformity

    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
