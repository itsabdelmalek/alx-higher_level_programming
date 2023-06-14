#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with keys sorted in alphabetical order.
    """
    # Get the sorted list of keys in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over each sorted key and print the key-value pair
    for key in sorted_keys:
        print(key + ": " + str(a_dictionary[key]))
