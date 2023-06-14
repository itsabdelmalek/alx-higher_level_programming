#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in a list.
    """
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over each element in the list
    for element in my_list:
        # Check if the element is an integer and add it to the set
        if isinstance(element, int):
            unique_integers.add(element)

    # Calculate the sum of unique integers
    total_sum = sum(unique_integers)

    return total_sum
