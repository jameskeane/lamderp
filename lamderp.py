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
  
    def __mul__(self, other):
        """Left Multiplication
        >>> map(_ * 2, [1, 2, 3])
        [2, 4, 6]
        """
        return self.binary(other, operator.mul)

    def __floordiv__(self, other):
        """Left floor division
        >>> map(_ // 2, [1, 2, 3])
        [0, 1, 1]
        """
        return self.binary(other, operator.floordiv)

    def __mod__(self, other):
        """Left Modulo operator
        >>> filter(_ % 2 == 1, range(10))
        [1, 3, 5, 7, 9]
        """
        return self.binary(other, operator.mod)

    def __divmod__(self, other):
        raise Exception('divmod is not currently supported')

    def __pow__(self, other):
        """Exponentiation operator
        >>> map(_ ** 2, [2, 3, 4])
        [4, 9, 16]
        """
        return self.binary(other, operator.pow)

    def __lshift__(self, other):
        """Left shift operator
        >>> map(_ << 2, [2, 3, 4])
        [8, 12, 16]
        """
        return self.binary(other, operator.lshift)

    def __rshift__(self, other):
        """Right shift operator
        >>> map(_ >> 2, [2, 3, 4])
        [0, 0, 1]
        """
        return self.binary(other, operator.rshift)

    def __and__(self, other):
        """Binary and operator
        >>> map(_ & 1, [1, 0])
        [1, 0]
        """
        return self.binary(other, operator.__and__)

    def __xor__(self, other):
        """Binary xor operator
        >>> map(_ ^ 1, [0, 1])
        [1, 0]
        """
        return self.binary(other, operator.xor)

    def __or__(self, other):
        """Binary or operator
        >>> map(_ | 1, [0, 1])
        [1, 1]
        """
        return self.binary(other, operator.__or__)

    def __div__(self, other):
        """Divison operator
        >>> map(_ / 2, [1, 2, 4, 8])
        [0, 1, 2, 4]
        """
        return self.binary(other, operator.div)

    def __truediv__(self, other):
        """Divison operator
        >>> from __future__ import division
        >>> map(_ / 2, [1, 2, 4, 8])
        [0, 1, 2, 4]
        """
        return self.binary(other, operator.truediv)

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

    def __rmul__(self, other):
        """Right Multiplication
        >>> map(2 * _, [1, 2, 3])
        [2, 4, 6]
        """
        return self.binary(other, operator.mul, right=True)

    def __rfloordiv__(self, other):
        """Right floor division
        >>> map(2 // _, [1, 2, 3])
        [2, 1, 0]
        """
        return self.binary(other, operator.floordiv, right=True)

    def __rmod__(self, other):
        """Right Modulo operator
        >>> map(2 % _, range(1, 5))
        [0, 0, 2, 2]
        """
        return self.binary(other, operator.mod, right=True)

    def __rdivmod__(self, other):
        raise Exception('divmod is not currently supported')

    def __rpow__(self, other):
        """Exponentiation operator
        >>> map(2 ** _, [2, 3, 4])
        [4, 8, 16]
        """
        return self.binary(other, operator.pow, right=True)

    def __rlshift__(self, other):
        """Right Left shift operator
        >>> map(2 << _, [2, 3, 4])
        [8, 16, 32]
        """
        return self.binary(other, operator.lshift, right=True)

    def __rrshift__(self, other):
        """Right Right shift operator
        >>> map(8 >> _, [2, 3, 4])
        [2, 1, 0]
        """
        return self.binary(other, operator.rshift, right=True)

    def __rand__(self, other):
        """Right Binary and operator
        >>> map(1 & _, [1, 0])
        [1, 0]
        """
        return self.binary(other, operator.__and__, right=True)

    def __rxor__(self, other):
        """Right Binary xor operator
        >>> map(1 ^ _, [0, 1])
        [1, 0]
        """
        return self.binary(other, operator.xor, right=True)

    def __ror__(self, other):
        """Right Binary or operator
        >>> map(1 | _, [0, 1])
        [1, 1]
        """
        return self.binary(other, operator.__or__, right=True)

    def __rdiv__(self, other):
        """Right Divison operator
        >>> map(8 / _, [1, 2, 4, 8])
        [8, 4, 2, 1]
        """
        return self.binary(other, operator.div, right=True)

    def __rtruediv__(self, other):
        """Right True Divison operator
        >>> from __future__ import division
        >>> map(8 / _, [1, 2, 4, 8])
        [8, 4, 2, 1]
        """
        return self.binary(other, operator.truediv, right=True)

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

    # Unary operations
    def __neg__(self):
        """Negation operator
        >>> map(- _, [1, 2, -3])
        [-1, -2, 3]
        """
        return self.unary(operator.neg)

    def __pos__(self):
        """Positive operator
        >>> map(+ _, [1, -2, 3])
        [1, -2, 3]
        """
        return self.unary(operator.pos)

    def __abs__(self):
        """Absolute value operator
        >>> map(abs(_), [1, -2, 3])
        [1, 2, 3]
        """
        return self.unary(operator.abs)

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
