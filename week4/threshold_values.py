def threshold_values(seq, threshold=1):
    """
    Threshold those values based upon their frequency and value.

    Args:
        seq (list): Results of random sampling
        threshold (int, optional): The frequencies kept to 1. Defaults to 1.
    """
    assert isinstance(seq, list) and isinstance(threshold, int) and threshold > 0
    bmap = {}
    for bs in seq:
        if bs in bmap:
            bmap[bs][1] += 1
        else:
            conv = 0 if sum(int(char) for char in bs) < len(bs) / 2 else 1
            bmap[bs] = [conv, 1]
    Ones = [[key, bmap[key][1]] for key in bmap if bmap[key][0] == 1]
    Ones.sort(key=lambda x: (x[1], -int(x[0])), reverse=True)
    highfreqs = set()
    for i in range(threshold):
        highfreqs.add(Ones[i][0])
    for key in bmap:
        if not bmap[key][1]:
            bmap[key] = 0
        else:
            if key in highfreqs:
                bmap[key] = 1
            else:
                bmap[key] = 0

    return bmap


x = [
    "10",
    "11",
    "01",
    "00",
    "10",
    "00",
    "00",
    "11",
    "10",
    "00",
    "00",
    "01",
    "01",
    "11",
    "10",
    "00",
    "11",
    "10",
    "11",
    "11",
]

# print(threshold_values(x, threshold=2))
