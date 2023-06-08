#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    import calculator_1

    result_sum = calculator_1.add(a, b)
    result_diff = calculator_1.subtract(a, b)
    result_mul = calculator_1.multiply(a, b)
    result_div = calculator_1.divide(a, b)

    print("The sum of {} and {} is: {}".format(a, b, result_sum))
    print("The difference between {} and {} is: {}".format(a, b, result_diff))
    print("The product of {} and {} is: {}".format(a, b, result_mul))
    print("The division of {} by {} is: {}".format(a, b, result_div))
