#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary.
    """
    # Check if the key exists in the dictionary before deleting
    if key in a_dictionary:
        del a_dictionary[key]
