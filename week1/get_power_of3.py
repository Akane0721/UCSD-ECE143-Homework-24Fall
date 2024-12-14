def get_power_of3(value):
    """
    Construct any number between 1 and 40 using a set of weights {1,3,9,27}.

    Args:
        value (int): The input value.
    """
    assert isinstance(value, int) and 1 <= value <= 40
    v = value
    weights = [1, 3, 9, 27]
    ans = []
    for i in range(4):
        if v % 3 == 0:
            a = 0
        elif v % 3 == 1:
            a = 1
        else:
            a = -1
        ans.append(a)
        v -= a * weights[i] / (3**i)
        v /= 3
    return ans


# print(get_power_of3(26))
