def get_average_word_length(words):
    """
    Compute the average length of the words

    Args:
        words (list): the list of words
    """
    assert isinstance(words, list)
    return sum(len(word) for word in words) / len(words)


def get_longest_word(words):
    """
    the longest word

    Args:
        words (list): the list of words
    """
    assert isinstance(words, list)
    return max(words, key=len)


def get_longest_words_startswith(words, start):
    """
    Get the longest word that starts with a single letter

    Args:
        words (list): the list of words
        start (str): the starting letter
    """
    assert isinstance(words, list) and isinstance(start, str)
    target_words = [word for word in words if word[0].lower() == start.lower()]
    return max(target_words, key=len)


def get_most_common_start(words):
    """
    Get the most common starting letter

    Args:
        words (list): the list of words
    """
    assert isinstance(words, list)
    freq = {}
    for word in words:
        if word[0] in freq:
            freq[word[0]] += 1
        else:
            freq[word[0]] = 1
    return max(freq, key=freq.get)


def get_most_common_end(words):
    """
    Get the most common ending letter

    Args:
        words (list): the list of words
    """
    assert isinstance(words, list)
    freq = {}
    for word in words:
        if word[-1] in freq:
            freq[word[-1]] += 1
        else:
            freq[word[-1]] = 1
    return max(freq, key=freq.get)


"""
with open("week2/google-10000-english-no-swears.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]
print(get_average_word_length(lines))
print(get_longest_word(lines))
print(get_longest_words_startswith(lines, "r"))
print(get_most_common_start(lines))
print(get_most_common_end(lines))"""
