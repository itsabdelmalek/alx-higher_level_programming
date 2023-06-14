#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set of elements present in only one set.
    """
    # Find the symmetric difference of the two sets
    diff_elements_set = set_1.symmetric_difference(set_2)

    return diff_elements_set
