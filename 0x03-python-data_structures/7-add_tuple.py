#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least 2 elements by extending or truncating them
    tuple_a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]

    # Add the first elements and the second elements separately
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Return a tuple with the sums
    return (sum_first, sum_second)

if __name__ == "__main__":
    # Example usage
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    result = add_tuple(tuple1, tuple2)
    print(result)
