#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == "__main__":
    # Example usage
    lst = [1, 5, 3, 8, 2, 7]
    result = max_integer(lst)
    print(result)
