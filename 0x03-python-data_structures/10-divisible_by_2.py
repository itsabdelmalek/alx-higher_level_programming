#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]

if __name__ == "__main__":
    # Example usage
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = divisible_by_2(lst)
    print(result)
