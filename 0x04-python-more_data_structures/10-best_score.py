#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in a dictionary.
    """
    # Check if the dictionary is empty
    if len(a_dictionary) == 0:
        return None

    # Initialize variables to keep track of the key with the maximum value
    max_key = None
    max_value = float('-inf')  # Initialize with a very small value

    # Iterate over each key-value pair in the dictionary
    for key, value in a_dictionary.items():
        # Check if the value is an integer and greater than the current value
        if isinstance(value, int) and value > max_value:
            max_key = key
            max_value = value

    return max_key
