#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return a set of common elements in two sets.
    """
    # Find the intersection of the two sets
    common_elements_set = set_1.intersection(set_2)

    return common_elements_set
