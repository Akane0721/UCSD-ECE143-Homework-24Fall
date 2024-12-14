import random


def multinomial_sample(n, p, k=1):
    """
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    """
    res = []
    assert isinstance(n, int) and isinstance(p, list) and isinstance(k, int)
    assert sum(p) == 1
    for i in range(k):
        sample = [0] * len(p)
        pick = random.choices(list(range(len(p))), weights=p, k=n)
        for pi in pick:
            sample[pi] += 1
        res.append(sample)
    return res


# print(multinomial_sample(10, [1 / 3, 1 / 3, 1 / 3], k=10))
