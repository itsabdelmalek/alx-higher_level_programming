#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                quotient = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError

            result.append(quotient)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)

        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        return result

    if __name__ == '__main__':

        list1 = [10, 20, 30]
        list2 = [5, 0, 2, 4]
        length = 5
        result_list = list_division(list1, list2, length)
        print(result_list)
