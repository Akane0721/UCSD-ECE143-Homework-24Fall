def compute_sum_to_n(n):
    """
    Compute the sum of all non-negative integers up to and including a specified value n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The sum of all integers from 0 to n, or 0 if n is negative.

    Raises:
        AssertionError: If the input is not a non-negative integer.
    """
    assert isinstance(n, int) and n >= 0, "Invalid Input."
    # if n <= 0:
    # return 0
    return (n + 1) * n // 2


# print(compute_sum_to_n(7))
