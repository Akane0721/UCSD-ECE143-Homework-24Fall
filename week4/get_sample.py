import random


def get_sample(nbits=3, prob=None, n=1):
    """
    Return a list n of random samples from a finite probability mass function defined by a dictionary with keys defined by a specified number of bits

    Args:
        nbits (int): Number of bits. Defaults to 3.
        prob (dict): Probability dictionary. Defaults to None.
        n (int): Number of samples. Defaults to 1.
    """
    assert isinstance(nbits, int) and nbits > 0
    assert isinstance(n, int) and n > 0
    assert isinstance(prob, dict) and sum(list(prob.values())) == 1
    expected_keys = {f"{i:0{nbits}b}" for i in range(2**nbits)}
    assert set(prob.keys()) == expected_keys

    keys = list(prob.keys())
    p = list(prob.values())
    samples = random.choices(keys, weights=p, k=n)
    return samples


pp = {
    "000": 0.125,
    "001": 0.125,
    "010": 0.125,
    "011": 0.125,
    "100": 0.125,
    "101": 0.125,
    "110": 0.125,
    "111": 0.125,
}

# print(get_sample(3, pp, 3))
