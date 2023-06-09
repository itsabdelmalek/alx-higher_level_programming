#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

if __name__ == "__main__":
    # Example usage
    lst = [1, 2, 3, 4, 5]
    index = 2
    new_element = 10
    result = replace_in_list(lst, index, new_element)
    print(result)
