def euclid(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


class Rational:
    def __init__(self, numerator, denominator):
        self._numerator = int(numerator)
        self._denominator = int(denominator)

    def __str__(self):
        return str(self._numerator) + "/" + str(self._denominator)

    def __add__(self, other):
        n = self.n*other.d+self.d*other.n
        d = self.d*other.d
        r = Rational(n, d)
        r.shortening()
        return r

    def __sub__(self, other):
        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        r = Rational(n, d)
        r.shortening()
        return r

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        r = Rational(n, d)
        r.shortening()
        return r

    def __truediv__(self, other):
        n = self.n * other.d
        d = self.d * other.n
        r = Rational(n, d)
        r.shortening()
        return r

    def __pow__(self, power, modulo=None):
        n = self.n
        d = self.d
        if modulo:
            print("Method __pow__ in Rational can't calculate modulo yet")
        else:
            for i in range(1, power):
                n *= self.n
                d *= self.d
        r = Rational(n, d)
        r.shortening()
        return r

    def shortening(self):
        divider = euclid(self.n, self.d)

        if min != 1:
            self.n = self.n // divider
            self.d = self.d // divider  # // dzielenie całkowite

    @property
    def n(self):
        return self._numerator

    @property
    def d(self):
        return self._denominator

    @n.setter
    def n(self, var):
        self._numerator = var

    @d.setter
    def d(self, var):
        self._denominator = var
