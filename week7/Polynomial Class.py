class Polynomial:
    def __init__(self, terms):
        """
        Initialize the Polynomial with a dictionary of terms.
        Keys are powers (integers), and values are coefficients (integers).
        """
        assert isinstance(terms, dict)
        assert all(isinstance(k, int) and k >= 0 for k in terms)
        assert all(isinstance(v, int) for v in terms.values())
        self.terms = {k: v for k, v in terms.items() if v != 0}

    def __repr__(self):
        if not self.terms:
            return "0"
        terms = []
        for power, coef in sorted(self.terms.items()):
            if power == 0:
                terms.append(f"{coef}")
            elif power == 1:
                if coef != 1:
                    terms.append(f"{coef} x")
                else:
                    terms.append("x")
            elif power > 1:
                if coef != 1:
                    terms.append(f"{coef} x^({power})")
                else:
                    terms.append(f"x^({power})")
        return " + ".join(terms).replace("+ -", "- ")

    def __add__(self, other):
        if isinstance(other, Polynomial):
            new_terms = self.terms.copy()
            for power, coef in other.terms.items():
                new_terms[power] = new_terms.get(power, 0) + coef
            return Polynomial(new_terms)
        elif isinstance(other, int):
            return self + Polynomial({0: other})
        else:
            raise TypeError("Integers and polynomials only!")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            new_terms = self.terms.copy()
            for power, coef in other.terms.items():
                new_terms[power] = new_terms.get(power, 0) - coef
            return Polynomial(new_terms)
        elif isinstance(other, int):
            return self - Polynomial({0: other})
        else:
            raise TypeError("Integers and polynomials only!")

    def __rsub__(self, other):
        if isinstance(other, int):
            return Polynomial({0: other}) - self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_terms = {}
            for p1, c1 in self.terms.items():
                for p2, c2 in other.terms.items():
                    power = p1 + p2
                    coef = c1 * c2
                    new_terms[power] = new_terms.get(power, 0) + coef
            return Polynomial(new_terms)
        elif isinstance(other, int):
            new_terms = {power: coef * other for power, coef in self.terms.items()}
            return Polynomial(new_terms)
        else:
            raise TypeError("Integers and polynomials only!")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        if not other.terms:
            raise ZeroDivisionError("Divided by zero")

        result = {}
        remainder = self.terms.copy()

        while remainder:
            highest_self = max(remainder)
            highest_other = max(other.terms)
            if highest_self < highest_other:
                break

            power_diff = highest_self - highest_other
            coef_diff = remainder[highest_self] // other.terms[highest_other]

            result[power_diff] = coef_diff

            for power, coef in other.terms.items():
                remainder[power + power_diff] = (
                    remainder.get(power + power_diff, 0) - coef * coef_diff
                )

            remainder = {k: v for k, v in remainder.items() if v != 0}

        if remainder:
            raise NotImplementedError(
                "Polynomial division resulted in a non-integer remainder."
            )

        return Polynomial(result)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.terms == other.terms
        elif isinstance(other, int):
            return self.terms == Polynomial({0: other}).terms
        return NotImplemented

    def subs(self, x):
        assert isinstance(x, int), "Substitution value must be an integer."
        return sum(coef * (x**power) for power, coef in self.terms.items())


"""
p = Polynomial({0: 8, 1: 2, 3: 4})  # keys are powers, values are coefficients
q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})
print(repr(p))
# 8 + 2 x + 4 x^(3)
print(p * 3)  # integer multiply
# 24 + 6 x + 12 x^(3)
print(3 * p)  # multiplication is commutative!
# 24 + 6 x + 12 x^(3)
print(p + q)  # add two polynomials
# 16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
print(p * 4 + 5 - 3 * p - 1)  # compose operations and add/subtract constants
# 12 + 2 x + 4 x^(3)
print(type(p - p))  # zero requires special handling but is still a Polynomial
# Polynomial
print(p * q)  # polynomial by polynomial multiplication works as usual
# 64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
print(p.subs(10))  # substitute in integers and evaluate
# 4028
print((p - p) == 0)
# True
print(p == q)
# False
p = Polynomial({0: 8, 1: 0, 3: 4})  # keys are powers, values are coefficients
print(repr(p))
#'8 + 4 x^(3)'
p = Polynomial({2: 1, 0: -1})
q = Polynomial({1: 1, 0: -1})
print(p / q)
# 1 + x
print(p / Polynomial({1: 1, 0: -3}))  # raises NotImplementedError
"""
