def write_chunks_of_five(words, fname):
    """
    Create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line

    Args:
        words (list): a list of words
        fname (str): name of the output file
    """
    assert isinstance(words, list) and isinstance(fname, str)
    res = []
    i = 0
    while i < len(words):
        if i + 5 > len(words):
            end = len(words)
        else:
            end = i + 5
        new_line = ""
        for w in words[i:end]:
            new_line += w
            new_line += " "
        new_line.rstrip()
        res.append(new_line)
        i = end
    with open(fname, "w", encoding="utf-8") as file:
        for line in res:
            file.write(f"{line}\n")


"""
with open("week2/google-10000-english-no-swears.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]
write_chunks_of_five(lines, "5_chunks.txt")"""
