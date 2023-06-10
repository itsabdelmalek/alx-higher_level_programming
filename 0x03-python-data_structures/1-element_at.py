#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ == "__main__":
    # Example usage
    lst = [1, 2, 3, 4, 5]
    index = 2
    result = element_at(lst, index)
    print(result)
