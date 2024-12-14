import math


def is_perfect(n):
    """
    Determines whether or not a strictly positive integer is perfect. A positive integer is perfect if the sum of all its proper divisors is equal to itself.

    Args:
        n (int): The input integer
    """
    assert isinstance(n, int) and n > 0
    if n == 1:
        return False
    list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            list.append(i)
        if n // i != i:
            list.append(n // i)
    # print(list)
    return 2 * n == sum(list)


# print(is_perfect(9))
