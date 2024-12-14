def next_permutation(t: tuple) -> tuple:
    """
    Given a permutation of any length, generate the next permutation in lexicographic order

    Args:
        t (tuple): Input permutation

    Returns:
        tuple: next permutation
    """
    assert isinstance(t, tuple)
    assert len(t) and len(t) == len(set(t))
    nums = list(t)
    l = len(nums)

    i = l - 1
    while i >= 1 and nums[i] <= nums[i - 1]:
        i -= 1
    if i == 0:
        return tuple(nums[::-1])
    j = l - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    nums[i:] = nums[i:][::-1]
    return tuple(nums)


# print(next_permutation((2, 3, 1)))
