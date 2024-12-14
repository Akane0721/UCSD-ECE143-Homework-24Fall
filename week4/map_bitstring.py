def map_bitstring(bitstrings):
    """
    Takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.

    Args:
        bitstrings (list): The list of bitstrings
    """
    assert isinstance(bitstrings, list)
    bmap = {}
    for bs in bitstrings:
        if bs not in bmap:
            bmap[bs] = 0 if sum(int(char) for char in bs) < len(bs) / 2 else 1
    return bmap


l = ["100", "100", "110", "010", "111", "000", "110", "010", "011", "000"]
# print(map_bitstring(l))
