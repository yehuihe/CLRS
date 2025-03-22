import random


def permute_by_sorting(A):
    """Randomly permuting arrays by sorting random priorities.

    # TODO: sorting A in place.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A sorted the elements of A according to these priorities.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of permute by sorting algorithm is:

    >>> A = [1, 2, 3, 4]
    >>> permute_by_sorting(A)
    [3, 2, 1, 4]

    Result is random.

    """
    n = len(A)
    P = [None] * n
    for i in range(n):
        P[i] = random.randint(1, n**3)
    return sorted(A, key=lambda x: P[A.index(x)])


def randomize_in_place(A):
    # TODO: currently wrong
    n = len(A)
    for i in range(n):
        A[i], A[random.randint(i, n-1)] = A[random.randint(i, n-1)], A[i]


def permute_without_identity(A):
    # TODO: currently wrong
    n = len(A)
    for i in range(n-1):
        A[i], A[random.randint(i+1, n - 2)] = A[random.randint(i+1, n - 2)], A[i]


def permute_with_all(A):
    # TODO: currently wrong
    n = len(A)
    for i in range(n):
        A[i], A[random.randint(1, n)] = A[random.randint(i, n)], A[i]


def permute_by_cyclic(A):
    pass


def random_sample(m, n):
    pass