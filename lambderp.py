import operator

class lambderp(object):
    def __init__(self):
        self.stack = []
        self.start = False

    def binary(self, other, op, right=False):
        if self.start is True:
            ret = lambderp()
        else:
            ret = self

        if type(other) == lambderp:
            if right:
                ret.stack.append(lambda x: op(other(x), x))
            else:
                ret.stack.append(lambda x: op(x, other(x)))
        else:
            if right:
                ret.stack.append(lambda x: op(other, x))
            else:
                ret.stack.append(lambda x: op(x, other))
        return ret

    def unary(self, op):
        self.stack.append(lambda x: op(x))
        return self

    def __add__(self, other):
        """Left addition
        >>> map(_ + 1, [1, 2, 3])
        [2, 3, 4]
        """
        return self.binary(other, operator.add)

    def __sub__(self, other):
        """Left subtraction
        >>> map(_ - 1, [1, 2, 3])
        [0, 1, 2]
        """
        return self.binary(other, operator.sub)     
  
    def __radd__(self, other):
        """Right addition
        >>> map(1 + _, [1, 2, 3])
        [2, 3, 4]
        """
        return self.binary(other, operator.add, right=True)

    def __rsub__(self, other):
        """Right subtraction
        >>> map(1 - _, [1, 2, 3])
        [0, -1, -2]
        """
        return self.binary(other, operator.sub, right=True)     

    def __mul__(self, other):
        """Left Multiplication
        >>> map(_ * 2, [1, 2, 3])
        [2, 4, 6]
        """
        return self.binary(other, operator.mul)

    def __rmul__(self, other):
        """Right Multiplication
        >>> map(2 * _, [1, 2, 3])
        [2, 4, 6]
        """
        return self.binary(other, operator.mul, right=True)

    def __lt__(self, other):
        """Less than operator
        >>> map(_ < 2, [1, 2, 3])
        [True, False, False]
        >>> map(2 < _, [1, 2, 3])
        [False, False, True]
        """
        return self.binary(other, operator.lt)

    def __le__(self, other):
        """Less than or equal to operator
        >>> map(_ <= 2, [1, 2, 3])
        [True, True, False]
        >>> map(2 <= _, [1, 2, 3])
        [False, True, True]
        """
        return self.binary(other, operator.le)

    def __eq__(self, other):
        """Equal to operator
        >>> map(_ == 2, [1, 2, 3])
        [False, True, False]
        >>> map(2 == _, [1, 2, 3])
        [False, True, False]
        """
        return self.binary(other, operator.eq)

    def __ne__(self, other):
        """Not equal to operator
        >>> map(_ != 2, [1, 2, 3])
        [True, False, True]
        >>> map(2 != _, [1, 2, 3])
        [True, False, True]
        """
        return self.binary(other, operator.ne)

    def __ge__(self, other):
        """Greater than or equal to operator
        >>> map(_ >= 2, [1, 2, 3])
        [False, True, True]
        >>> map(2 >= _, [1, 2, 3])
        [True, True, False]
        """
        return self.binary(other, operator.ge)

    def __gt__(self, other):
        """Greater than operator
        >>> map(_ > 2, [1, 2, 3])
        [False, False, True]
        >>> map(2 > _, [1, 2, 3])
        [True, False, False]
        """
        return self.binary(other, operator.gt)

    def __mod__(self, other):
        """Left Modulo operator
        >>> filter(_ % 2 == 1, range(10))
        [1, 3, 5, 7, 9]
        """
        return self.binary(other, operator.mod)

    def __rmod__(self, other):
        """Right Modulo operator
        >>> filter(2 % _ == 1, range(10))
        [1, 3, 5, 7, 9]
        """
        return self.binary(other, operator.mod, right=True)

    #def __not__(self):
    #    return self.unary(operator.__not__)

    def __call__(self, arg):
        self.stack.insert(0, lambda x: x)  # Push an identity
        res = arg
        for f in self.stack:
            res = f(res)
        return res

_ = lambderp()
_.start = True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
