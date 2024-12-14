def convert_hex_to_RGB(hex_list):
    """
    Convert a list of color hex-codes into a list of RGB-tuples.

    Args:
        hex_list(list): A list of strings representing color hex-code

    Returns:
        A list of RGB-tuples corresponds to the hex-code

    Raises:
        Assertion Error: If the input is not a list with length of 7
    """
    res = []
    for hexcode in hex_list:
        assert isinstance(hexcode, str) and len(hexcode) == 7, "Invalid Input."
        r = int(hexcode[1:3], 16)
        g = int(hexcode[3:5], 16)
        b = int(hexcode[5:7], 16)
        res.append((r, g, b))
    return res
