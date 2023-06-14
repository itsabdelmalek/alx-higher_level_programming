#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.
    """
    # Update the value of the key if it exists, or add a new key/value pair
    a_dictionary[key] = value
    return (a_dictionary)
