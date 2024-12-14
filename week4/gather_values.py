def gather_values(x):
    """
    Generate n samples and tally the number of times an existing key is repeated. Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped values from map_bitstring

    Args:
        x (list): The list of bitstrings
    """
    assert isinstance(x, list)
    bmap = {}
    for bs in x:
        conv = 0 if sum(int(char) for char in bs) < len(bs) / 2 else 1
        if bs not in bmap:
            bmap[bs] = [conv]
        else:
            bmap[bs].append(conv)
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

# print(gather_values(x))
