# fill out the necessary methods shown below and add others if need be.


class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        return f"Interval({self._a}, {self._b})"

    def __eq__(self, other):
        assert isinstance(other, Interval)
        return self._a == other._a and self._b == other._b

    def __lt__(self, other):
        assert isinstance(other, Interval)
        return self._b < other._b and self._a < other._a

    def __gt__(self, other):
        assert isinstance(other, Interval)
        return self._b > other._b and self._a > other._a

    def __ge__(self, other):
        assert isinstance(other, Interval)
        return self._b >= other._b and self._a >= other._a

    def __le__(self, other):
        assert isinstance(other, Interval)
        return self._b <= other._b and self._a <= other._a

    def __add__(self, other):
        assert isinstance(other, Interval)
        if self._b <= other._a or self._a >= other._b:
            return [self, other]
        self._a = min(self._a, other._a)
        self._b = max(self._b, other._b)
        return self
