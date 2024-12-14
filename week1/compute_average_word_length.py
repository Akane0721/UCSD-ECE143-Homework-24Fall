def compute_average_word_length(instring, unique=False):
    """
    Compute the average length of the words in the input string

    Args:
        instring (str): The input string.
        unique (bool, optional): If the unique option is True, then exclude duplicated words. Defaults to False.
    """
    assert isinstance(instring, str) and isinstance(unique, bool)
    words = instring.split(" ")
    if unique:
        words = list(set(words))

    ans = 0
    for w in words:
        ans += len(w)
    return ans / len(words)


'''
string = """Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go"""
print(compute_average_word_length(string, True))
'''
