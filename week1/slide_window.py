def slide_window(x, width, increment):
    """
    Take the window width and the window increment as inputs and produce a sequence of overlapping lists from the input list.

    Args:
        x (list): The input list.
        width (int): Window size.
        increment (int): Window increment
    """
    assert (
        isinstance(x, list)
        and isinstance(width, int)
        and isinstance(increment, int)
        and width > 0
        and increment > 0
    )
    res = []
    i = 0
    while i < len(x) - width + 1:
        res.append(x[i : i + width])
        i += increment

    return res


# print(slide_window(list(range(18)), 5, 2))
