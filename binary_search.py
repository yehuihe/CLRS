"""
Solution to Exercise 2.3-5
"""

def linear_search(A, v):
    """

    Exercise 2.1-3

    Parameters
    ----------
    A : list, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    v : int
        Value to search for

    Returns
    -------


    """

    for i in range(0, len(A)):
        if A[i] == v:
            return i
    return -1


def iterative_binary_search(A, v, low, high):
    while low <= high:
        mid = (low + high) // 2
        if v == A[mid]:
            return mid
        elif v > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def recursive_binary_search(A, v, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if v == A[mid]:
        return mid
    if v > A[mid]:
        return recursive_binary_search(A, v, mid + 1, high)
    else:
        return recursive_binary_search(A, v, low, mid - 1)


