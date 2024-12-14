import math


class Rational:
    def __init__(self, numerator, denominator):
        assert isinstance(numerator, int) and isinstance(denominator, int)
        assert denominator != 0

        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        if self.denominator != 1:
            return f"{self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}"

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            num = (
                self.numerator * other.denominator + other.numerator * self.denominator
            )
            den = self.denominator * other.denominator
        else:
            num = self.numerator + other * self.denominator
            den = self.denominator
        return Rational(num, den)

    def __sub__(self, other):
        if isinstance(other, Rational):
            num = (
                self.numerator * other.denominator - other.numerator * self.denominator
            )
            den = self.denominator * other.denominator
        else:
            num = self.numerator - other * self.denominator
            den = self.denominator
        return Rational(num, den)

    def __mul__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
        else:
            num = self.numerator * other
            den = self.denominator
        return Rational(num, den)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
        else:
            num = self.numerator
            den = self.denominator * other
        return Rational(num, den)

    def __rtruediv__(self, other):
        num = self.denominator * other
        den = self.numerator
        return Rational(num, den)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)


def square_root_rational(x, abs_tol=Rational(1, 1000)):
    """
    Takes an input rational number x and returns the square root of x to absolute precision abs_tol

    Args:
        x (Rational): Input rational number
        abs_tol (Rational): Tolerance, defaults to Rational(1, 1000).
    """
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)
    assert x.numerator >= 0

    low = Rational(0, 1)
    high = x

    while True:
        mid = low + (high - low) / 2
        mid_squared = mid * mid

        if abs(mid_squared - x) < abs_tol:
            return mid

        if mid_squared < x:
            low = mid
        else:
            high = mid


# print(square_root_rational(Rational(1112, 3), abs_tol=Rational(1, 1000)))
