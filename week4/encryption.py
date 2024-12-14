from collections import defaultdict
import random


def encrypt_message(message, fname):
    """
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    """
    assert isinstance(message, str) and isinstance(fname, str)
    pw_table = defaultdict(list)

    with open(fname, "r") as file:
        for r, line in enumerate(file):
            for c, word in enumerate(line.split()):
                pw_table[word].append((r, c))

    msg = message.split()
    used = set()
    encryption = []
    for m in msg:
        w = random.choice(pw_table[m])
        while w in used:
            w = random.choice(pw_table[m])
        assert w not in used
        encryption.append(w)
        used.add(w)

    return encryption


def decrypt_message(inlist, fname):
    """
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.

    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    """
    assert isinstance(inlist, list) and isinstance(fname, str)
    assert all(isinstance(c, tuple) for c in inlist)
    pw_table = []
    decryption = []
    with open(fname, "r") as file:
        for line in file:
            pw_table.append(line.split())
    for r, c in inlist:
        decryption.append(pw_table[r][c])
    return " ".join(decryption)


"""
msg = "let us not say we met late at the night about the secret"
c = encrypt_message(msg, "pg5200.txt")
print(c)
m = decrypt_message(c, "pg5200.txt")
print(m)
"""
