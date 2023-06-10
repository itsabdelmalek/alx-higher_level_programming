#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    # Example usage
    lst = [1, 2, 3, 4, 5]
    index = 2
    new_element = 10
    result = new_in_list(lst, index, new_element)
    print(result)
