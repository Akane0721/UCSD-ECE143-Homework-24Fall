def get_trapped_water(seq):
    """
    Compute how many units of water remain trapped between the walls in the map

    Args:
        seq (list): A two-dimensional elevation map where each element is unit-width wall and the integer value is the height
    """
    assert isinstance(seq, list)
    l = len(seq)
    if l == 1:
        return 0
    pre = [0] * l
    aft = [0] * l
    for i in range(1, l):
        pre[i] = max(seq[i - 1], pre[i - 1])
        aft[l - 1 - i] = max(seq[l - i], aft[l - i])
    ans = 0
    for i in range(l):
        waterline = min(pre[i], aft[i])
        depth = max(waterline - seq[i], 0)
        ans += depth
    return ans


# print(get_trapped_water([2, 1, 2]))
