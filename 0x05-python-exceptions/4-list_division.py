#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # pycodestyle will check for code style conformity

    result = []
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                division_result = 0  # Default value if division cannot be done

                if isinstance(dividend, (int, float))
                and isinstance(divisor, (int, float)):
                    try:
                        division_result = dividend / divisor
                    except ZeroDivisionError:
                        print("division by 0")
                else:
                    print("wrong type")

                result.append(division_result)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
