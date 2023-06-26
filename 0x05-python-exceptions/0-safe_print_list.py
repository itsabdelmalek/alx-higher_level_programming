#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # pycodestyle will check for code style conformity

    # Using a try-except block to handle exceptions
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
