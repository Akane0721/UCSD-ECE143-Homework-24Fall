from time import sleep
import random
from datetime import datetime
import itertools as it
from types import GeneratorType


def producer():
    "produce timestamps"
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime


def tracker(producer, limit=1):
    """
    A generator that tracks the output of the producer and ultimately returns the number of odd numbered seconds that have been iterated over

    Args:
        producer (func): A generator that returns the duration of its lifetime when called
        limit (int): The number of odd-numbered seconds to track until completion

    Yields:
        int: number of odd-numbered seconds
    """
    assert isinstance(producer, GeneratorType) and isinstance(limit, int)
    count = 0

    for timestamp in producer:
        # print("t:", timestamp.seconds)
        if timestamp.seconds % 2 != 0:
            count += 1

        new_limit = yield count
        if new_limit is not None:
            limit = new_limit

        if count >= limit:
            break


"""
p = producer()
t = tracker(p, limit=3)
print(type(t))

next(t)
next(t)
t.send(5)
print(list(t))
"""
