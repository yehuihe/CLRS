from abc import ABCMeta, abstractmethod
import math
import random

__all__ = ["DivisionMethod",
           "MultiplicationMethod",
           "UniversalClass",
           "LinearProbing",
           "QuadraticProbing",
           "DoubleHashing"]

A_KNUTH = (math.sqrt(5) - 1) / 2


class BaseHashFunction(metaclass=ABCMeta):
    """Base class for hash functions."""

    def __init__(self, m):
        self.m = m

    @abstractmethod
    def h(self):
        """
        Hash function.

        Returns
        -------
        h : method
            The hash function h.

        """
        pass


class DivisionMethod(BaseHashFunction):
    """The division method for creating hash functions

    Parameters
    ----------
    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    Returns
    -------
    h(k) : int
        The hash value of key k.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Notes
    -----
    We usually avoid certain values of m. For example, m should not be a power of 2.
    A prime not too close to an exact power of 2 is often a good choice for m.
    See CLRS p.263.

    Examples
    --------
        A simple application of the division method is:

    >>> m = 12
    >>> k = 100
    >>> h = DivisionMethod(m).h()
    >>> h(k)
    4

    """

    def __init__(self, m):
        super().__init__(m)

    def h(self):
        """The division method for creating hash functions.

        Returns
        -------
        h : method
            The hash function h.

        """
        h = lambda k: k % self.m
        return h


class MultiplicationMethod(BaseHashFunction):
    """The multiplication method for creating hash functions

    Parameters
    ----------
    A : float, default=A_KNUTH
        Constant A in the range 0 < A < 1.

    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    Returns
    -------
    h(k) : int
        The hash value of key k.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    .. [2] Donald E. Knuth. Sorting and Searching, volume 3 of The Art of Computer Programming.
        Addison-Wesley, 1973. Second edition, 1998.

    Notes
    -----
    Default value of A is Knuth [2] suggests that A=(\sqrt(4)-1)/2=0:6180339887.

    Examples
    --------
    A simple application of the division method is:

    >>> m = 2**14
    >>> k = 123456
    >>> h = MultiplicationMethod(m).h()
    >>> h(k)
    67

    CLRS Exercise 11.3-4:

    >>> m = 1000
    >>> k = [61, 62, 63, 64, 65]
    >>> h = MultiplicationMethod(m).h()
    >>> for i in map(h, k):
    ...    print(i)
    700
    318
    936
    554
    172

    """
    def __init__(self, m, A=A_KNUTH):
        super().__init__(m)
        self.A = A

    def h(self):
        """The multiplication method for creating hash functions.

        Returns
        -------
        h : method
            The hash function h.

        """
        h = lambda k: math.floor(self.m * (k * self.A % 1))
        return h
        # return math.floor(m * (k * A % 1))


class UniversalClass(BaseHashFunction):
    """The universal hashing method for creating hash functions

    Parameters
    ----------
    k : int
        key k.

    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    p : int
        A prime number p large enough so that every possible
        key k is in the range 0 to p-1, inclusive.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Notes
    -----
    Default value of A is Knuth [2] suggests that A=(\sqrt(4)-1)/2=0:6180339887.

    Examples
    --------
    A simple application of the UniversalClass is:

    >>> m = 6
    >>> k = 8
    >>> p = 17
    >>> H_pm = UniversalClass(m, p)
    >>> h, a, b = H_pm.h()
    >>> print(a, b)
    14 4
    >>> h(k)
    2

    """

    def __init__(self, m, p):
        super().__init__(m)
        self.p = p

    def h(self):
        """One hash function in the family.

        Returns
        -------
        h : method
            The hash function h_ab.

        a : int
            a in the set Z_p* denote the set {1,2,...,p-1}.

        b : int
            b in the set Z_p denote the set {0,1,...,p-1}.
        """
        a = random.randint(1, self.p - 1)  # Z_p* denote the set {1,2,...,p-1}
        b = random.randint(0, self.p - 1)  # Z_p denote the set {0,1,...,p-1}

        h = lambda k: ((a*k + b) % self.p) % self.m
        return h, a, b
        # def h(k):
        #     return ((a*k + b) % self.p) % self.m
        #
        # return h, a, b


class LinearProbing(BaseHashFunction):
    """
    Linear Probing technique to compute the probe sequences
    required for open addressing.

    Parameters
    ----------
    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    h_prime : func
        Auxiliary hash function

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the LinearProbing is:

    >>> m = 11
    >>> k = 28
    >>> h_prime = lambda k: k
    >>> h = LinearProbing(m, h_prime).h()
    >>> h(k, 0)
    6
    >>> h(k, 1)
    7

    """

    def __init__(self, m, h_prime):
        super().__init__(m)
        self.h_prime = h_prime

    def h(self):
        """Linear probing hash function.

        Returns
        -------
        h : method
            The hash function h.

        """
        h = lambda k, i: (self.h_prime(k) + i) % self.m
        return h


class QuadraticProbing(BaseHashFunction):
    """
    Quadratic Probing technique to compute the probe sequences
    required for open addressing.

    Parameters
    ----------
    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    c_1 : int
        Positive auxiliary constant.

    c_2 : int
        Positive auxiliary constant.

    h_prime : func
        Auxiliary hash function

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the QuadraticProbing is:

    >>> m = 11
    >>> k = 28
    >>> h_prime = lambda k: k
    >>> c_1 = 1
    >>> c_2 = 3
    >>> h = QuadraticProbing(m, c_1, c_2, h_prime).h()
    >>> h(k, 0)
    6
    >>> h(k, 1)
    7
    >>> h(k, 2)
    9

    """

    def __init__(self, m, c_1, c_2, h_prime):
        super().__init__(m)
        self.c_1 = c_1
        self.c_2 = c_2
        self.h_prime = h_prime

    def h(self):
        """Quadratic probing hash function.

        Returns
        -------
        h : method
            The hash function h.

        """
        h = lambda k, i: (self.h_prime(k) +
                          self.c_1*i + self.c_2*i**2) % self.m
        return h


class DoubleHashing(BaseHashFunction):
    """
    Double hashing technique to compute the probe sequences
    required for open addressing.

    Parameters
    ----------
    m : int
        Slots of a hash table T[0..m-1]. m slots of the hash table.

    h_1 : func
        First auxiliary hash function.

    h_2 : func
        Second auxiliary hash function.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the DoubleHashing is:

    >>> m = 13
    >>> k = 14
    >>> h_1 = DivisionMethod(m).h()
    >>> h_2 = lambda k: 1 + k % 11
    >>> h = DoubleHashing(m, h_1, h_2).h()
    >>> h(k, 0)
    1
    >>> h(k, 1)
    5
    >>> h(k, 2)
    9

    """

    def __init__(self, m, h_1, h_2):
        super().__init__(m)
        self.h_1 = h_1
        self.h_2 = h_2

    def h(self):
        """Double hashing hash function.

        Returns
        -------
        h : method
            The hash function h.

        """
        h = lambda k, i: (self.h_1(k) + i*self.h_2(k)) % self.m
        return h
