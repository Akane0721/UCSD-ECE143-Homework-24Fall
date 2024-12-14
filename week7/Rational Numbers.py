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


"""
if __name__ == "__main__":
    r = Rational(3, 4)
    print(repr(r))  # '3/4'
    print(-1 / r)  # -4/3
    print(float(-1 / r))  # -1.3333333333333333
    print(int(r))  # 0
    print(int(Rational(10, 3)))  # 3
    print(Rational(10, 3) * Rational(101, 8) - Rational(11, 8))  # 977/24
    print(
        sorted([Rational(10, 3), Rational(9, 8), Rational(10, 1), Rational(1, 100)])
    )  # [1/100, 9/8, 10/3, 10]
    print(Rational(100, 10))  # 10
    print(
        -Rational(12345, 128191) + Rational(101, 103) * 30 / 44
    )  # 166235595/290480806
"""
