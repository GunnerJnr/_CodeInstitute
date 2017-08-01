class Fraction:
    def __repr__(self):
        return '%s/%s' % (self.num, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)
 
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
 
    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)
