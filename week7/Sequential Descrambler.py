import itertools
from collections import defaultdict, Counter


def load_dictionary(file_path):

    word_map = defaultdict(list)
    with open(file_path, "r") as f:
        for word in f:
            word = word.strip()
            word_map[len(word)].append((word, Counter(word)))
    return word_map


def descrambler(w, k):
    """
    Generate valid phrases from scrambled sequence `w` and partition lengths `k`

    Args:
        w (str): Input string
        k (tuple): Tuple of integers that indicate partition-lengths of the sequence
    """
    assert isinstance(w, str) and isinstance(k, tuple)
    word_map = load_dictionary("/tmp/google-10000-english-no-swears.txt")
    wc = Counter(w)
    result = []

    def backtrack(idx, remaining, phrases):
        if idx == len(k):
            yield " ".join(phrases)
            return
        word_len = k[idx]
        for word, word_counter in word_map[word_len]:
            if all(remaining[char] >= count for char, count in word_counter.items()):
                new_remaining = remaining - word_counter
                yield from backtrack(idx + 1, new_remaining, phrases + [word])

    return backtrack(0, wc, [])


"""
if __name__ == "__main__":
    print(
        list(descrambler("trleeohelh", (5, 5)))
    )  # ['hello three', 'three hello', 'hello there', 'there hello']
    print(
        list(descrambler("choeounokeoitg", (3, 5, 6)))
    )  # ['one tough cookie', 'one ought cookie', ...]
    print(
        list(descrambler("qeodwnsciseuesincereins", (4, 7, 12)))
    )  # ['wise insider consequences']
    s = descrambler("choeounokeoitg", (3, 5, 6))
    print(s)
    print(type(s))
    print(next(s))
    print(next(s))

    c = Counter("qeodwnsciseuesincereins")
    print(c)
    print("".join(c.elements()))
    print(c.items())
    """
