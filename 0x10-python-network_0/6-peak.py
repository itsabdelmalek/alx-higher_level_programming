#!/usr/bin/python3
"""Defines a peak finding code."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): List of unsorted integers.

    Returns:
    int: A peak from the list.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
