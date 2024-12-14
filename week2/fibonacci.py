def fibonacci(n):
    """
    A generator to compute the first n Fibonacci numbers: F[n] = F[n-1]+F[n-2]

    Args:
        n (int): queue length
    """
    assert isinstance(n, int) and n > 0
    pre = 1
    cur = 1
    for _ in range(n):
        yield pre
        after = pre + cur
        pre = cur
        cur = after
