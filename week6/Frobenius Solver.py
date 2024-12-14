import numpy as np


def solvefrob(coefs, b):
    """
    Solve the frobenius equation

    Args:
        coefs (list): the list of a_i coefficients
        b (int): A positive integer
    """
    assert isinstance(coefs, list) and isinstance(b, int)
    n = len(coefs)
    max_x = [b // a for a in coefs]
    grid = np.indices([max_x[i] + 1 for i in range(n)])
    x_combinations = grid.reshape(n, -1).T
    multiply = np.dot(x_combinations, coefs)
    valid = x_combinations[multiply == b]
    res = [tuple(combination) for combination in valid]
    return res


# print(solvefrob([1, 2, 3, 5], 10))
