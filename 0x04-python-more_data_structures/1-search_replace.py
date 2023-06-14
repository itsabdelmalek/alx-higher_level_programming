#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a new list.
    """
    # Create a new list to store the modified elements
    new_list = []

    # Iterate over each element in the original list
    for element in my_list:
        # Check if the element matches the search element
        if element == search:
            # Replace the element with the new element
            new_list.append(replace)
        else:
            # Keep the element as is
            new_list.append(element)

    return new_list
