import math
from operator import ge, le
from random import randrange
# from ..data_structures import MaxHeap
from data_structures import MaxHeap

__all__ = ["bubble_sort", "insertion_sort", "selection_sort",
           "merge", "merge_sort", "heap_sort",
           "partition", "quicksort", "randomized_partition",
           "randomized_quicksort", "hoare_partition", "hoare_quicksort",
           "counting_sort", "radix_sort"]


# TODO: quicksort always using modified_tail_recursive_quicksort
# TODO: implementing Robert Sedgewick's paper practice


def bubble_sort(A):
    """Bubble sort algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the bubble sort algorithm is:

    >>> A = [5, 2, 4, 6, 1, 3]
    >>> bubble_sort(A)
    >>> A
    [1, 2, 3, 4, 5, 6]

    """
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


def insertion_sort(A, reverse=False):
    """Insertion sort algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the insertion sort algorithm is:

    >>> A = [5, 2, 4, 6, 1, 3]
    >>> insertion_sort(A)
    >>> A
    [1, 2, 3, 4, 5, 6]

    Sort in descending order:

    >>> A = [5, 2, 4, 6, 1, 3]
    >>> insertion_sort(A, reverse=True)
    >>> A
    [6, 5, 4, 3, 2, 1]

    >>> A = [31, 41, 59, 26, 41, 58]
    >>> insertion_sort(A)
    >>> A
    [26, 31, 41, 41, 58, 59]

    """
    op = le if reverse else ge
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1..j-1].
        i = j - 1
        while i >= 0 and op(A[i], key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def selection_sort(A):
    """
    Selection sort algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the selection sort algorithm is:

    >>> A = [5, 2, 4, 6, 1, 3]
    >>> selection_sort(A)
    >>> A
    [1, 2, 3, 4, 5, 6]

    """
    for j in range(len(A)-1):
        smallest = j
        for i in range(j + 1, len(A)):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]


def merge(A, p, q, r):
    """
    Auxiliary procedure MERGE.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    p : int
        Starting index.

    q : int
        Split index.

    r : int
        Ending index.

    Returns
    -------
    A : ndarray, shape (n,)
        It merges two sorted subarrays A[p..q] and A[q+1..r] to form a single sorted subarray
        that replaces the current subarray.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the insertion sort algorithm is:

    >>> A = [2, 7, 4, 5, 2, 3, 6, 5, 2, 4, 5, 7, 1, 2, 3, 6, 9]
    >>> _merge(A, 8, 11, 15)
    >>> A
    [2, 7, 4, 5, 2, 3, 6, 5, 1, 2, 2, 3, 4, 5, 6, 7, 9]

    """
    n1 = q - p + 1
    n2 = r - q
    L = [A[p + i] for i in range(0, n1)]
    R = [A[q + j + 1] for j in range(0, n2)]
    # Sentinel
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    """
    Merge sort algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    p : int
        Starting index.

    r : int
        Ending index.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the insertion sort algorithm is:

    >>> A = [5, 2, 4, 7, 1, 3, 2, 6]
    >>> merge_sort(A, 0, 7)
    >>> A
    [1, 2, 2, 3, 4, 5, 6, 7]

    """
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def partition(A, p, r, reverse=False):
    """
    Auxiliary PARTITION procedure for quicksort.

    Parameters
    ----------
    A : list, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    p : int
        Starting index.

    r : int
        Ending index.

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

    Returns
    -------
    q : int
        The index q as part of this partitioning procedure.
        A[q] is strictly less than every element of A[q+1..r].

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the partition is:

    >>> A = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> q = partition(A, 0, 7)
    >>> q
    3
    >>> A
    [2, 1, 3, 4, 7, 5, 6, 8]

    Another example (in Lecture Notes)
    >>> A = [8, 1, 6, 4, 0, 3, 9, 5]
    >>> q = partition(A, 0, 7)
    >>> q
    4
    >>> A
    [2, 1, 3, 4, 7, 5, 6, 8]

    Exercises 7.1-1
    >>> A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    >>> q = partition(A, 0, 11)
    >>> q
    7
    >>> A
    [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]

    """
    x = A[r]
    i = p - 1
    op = ge if reverse else le
    for j in range(p, r):
        if op(A[j], x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quicksort(A, p, r, reverse=False):
    """
    QUICKSORT algorithm.

    # TODO: implementing Robert Sedgewick's paper practice

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    p : int
        Starting index.

    r : int
        Ending index.

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    .. [2] Robert Sedgewick. Implementing quicksort programs. Communications of the ACM,
        21(10):847–857, 1978.

    Examples
    --------
        A simple application of the quicksort algorithm is:

    >>> A = [5, 2, 4, 7, 1, 3, 2, 6]
    >>> quicksort(A, 0, 7)
    >>> A
    [1, 2, 2, 3, 4, 5, 6, 7]

    nonincreasing order:

    >>> A = [5, 2, 4, 7, 1, 3, 2, 6]
    >>> quicksort(A, 0, 7, reverse=True)
    >>> A
    [7, 6, 5, 4, 3, 2, 2, 1]

    """
    if p < r:
        q = partition(A, p, r, reverse)
        quicksort(A, p, q-1, reverse)
        quicksort(A, q+1, r, reverse)


def tail_recursive_quicksort(A, p, r, reverse=False):
    """
    TAIL-RECURSIVE-QUICKSORT procedure

    See also
    --------
    partition : For documentation for the rest of the parameters, see partition

    Notes
    -----
    See CLRS Problems 7.4

    """
    if p < r:
        # Partition and sort left subarray.
        q = partition(A, p, r, reverse)
        tail_recursive_quicksort(A, p, q-1, reverse)
        p = q + 1


def modified_tail_recursive_quicksort(A, p, r, reverse=False):
    """
    Modified TAIL-RECURSIVE-QUICKSORT procedure

    # TODO: quicksort always using modified_tail_recursive_quicksort
    # for better worst-case stack depth

    The worst-case stack depth is O(lg n).

    See also
    --------
    partition : For documentation for the rest of the parameters, see partition

    Notes
    -----
    See CLRS Problems 7.4

    """
    while p < r:
        # Partition and sort the small subarray first.
        q = partition(A, p, r, reverse)
        if q - p < r - q:
            modified_tail_recursive_quicksort(A, p, q-1, reverse)
            p = q + 1
        else:
            modified_tail_recursive_quicksort(A, q+1, r, reverse)
            r = q - 1


def randomized_partition(A, p, r, reverse=False):
    """
    RANDOMIZED-PARTITION procedure for

    See also
    --------
    partition : For documentation for the rest of the parameters, see partition

    """
    i = randrange(p, r + 1)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r, reverse)


def randomized_quicksort(A, p, r, reverse=False):
    """
    RANDOMIZED-QUICKSORT algorithm.

    See also
    --------
    quicksort : For documentation for the rest of the parameters, see quicksort

    """
    if p < r:
        q = randomized_partition(A, p, r, reverse)
        randomized_quicksort(A, p, q-1, reverse)
        randomized_quicksort(A, q+1, r, reverse)


def hoare_partition(A, p, r, reverse=False):
    """
    Auxiliary HOARE-PARTITION procedure for Hoare quicksort.

    See also
    --------
    partition : For documentation for the rest of the parameters, see partition

    Examples
    --------
    A simple application of the hoare partition is:

    >>> A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    >>> q = hoare_partition(A, 0, 11)
    >>> q
    8
    """
    x = A[p]
    i = p - 1
    j = r + 1
    op1, op2 = (ge, le) if reverse else (le, ge)
    while True:
        while True:
            j -= 1
            if op1(A[j], x):
                break
        while True:
            i += 1
            if op2(A[i], x):
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j


def hoare_quicksort(A, p, r, reverse=False):
    """
    HOARE-QUICKSORT algorithm.

    See also
    --------
    quicksort : For documentation for the rest of the parameters, see quicksort

    Examples
    --------
    A simple application of the hoare quicksort algorithm is:

    >>> A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    >>> hoare_quicksort(A, 0, 11)
    >>> A
    [2, 4, 5, 6, 7, 8, 9, 12, 11, 13, 19, 21]

    nonincreasing order:

    >>> A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    >>> hoare_quicksort(A, 0, 11, reverse=True)
    >>> A
    [21, 19, 13, 11, 12, 9, 8, 7, 5, 6, 4, 2]

    """
    if p < r:
        q = hoare_partition(A, p, r, reverse)
        hoare_quicksort(A, p, q - 1, reverse)
        hoare_quicksort(A, q + 1, r, reverse)


def heap_sort(A):
    """
    Heap sort algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the heap sort algorithm is:

    >>> A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    >>> heap_sort(A)
    >>> A
    [2, 4, 5, 7, 8, 13, 17, 20, 25]

    """
    max_heap = MaxHeap(A, len(A))
    max_heap.build_max_heap()
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heap._heap_size -= 1
        max_heap.max_heapify(0)
        # print(A)


def counting_sort(A, B, k, reverse=False):
    """
    COUNTING-SORT algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    B : ndarray, shape (n,)
        The array B[1..n] holds the sorted output.

    k : int
        Each of the n input elements is an integer in the range 0 to k.
        Range of A.

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

    Returns
    -------
    B : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the counting sort algorithm is:

    >>> A = [2, 5, 3, 0, 2, 3, 0, 3]
    >>> B = [None] * len(A)
    >>> counting_sort(A, B, max(A))
    >>> B
    [0, 0, 2, 2, 3, 3, 3, 5]

    Another example from CLRS exercises 8.2-1

    >>> A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    >>> B = [None] * len(A)
    >>> counting_sort(A, B, max(A))
    >>> B
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6]

    Sort in descending order:
    >>> A = [2, 5, 3, 0, 2, 3, 0, 3]
    >>> B = [None] * len(A)
    >>> counting_sort(A, B, max(A), reverse=True)
    >>> B
    [5, 3, 3, 3, 2, 2, 0, 0]

    """
    n = len(A)
    C = [0] * (k + 1)
    for j in range(n):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i.
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    # C[i] now contains the number of elements less than or equal to i.
    for j in range(n-1, -1, -1):
        if reverse:
            B[n - C[A[j]]] = A[j]
        else:
            B[C[A[j]] - 1] = A[j]  # B python offset 1
        C[A[j]] -= 1


def radix_sort(A):
    """
    COUNTING-SORT algorithm.

    # TODO: reverse option. Order is wrong
    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    B : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an') such that
        a1' <= a2', ..., <= an'.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the radix sort algorithm is:

    >>> A = [329, 457, 657, 839, 436, 720, 355]
    >>> B = radix_sort(A)
    >>> B
    [329, 355, 436, 457, 657, 720, 839]

    Another example from CLRS Instructor Manual

    >>> A = [326, 453, 608, 835, 751, 435, 704, 690]
    >>> B = radix_sort(A)
    >>> B
    [326, 435, 453, 608, 690, 704, 751, 835]

    Another example with nonuniform digits numbers

    >>> A = [123, 24, 345, 6, 567, 678, 76, 44,
             357, 10, 234, 555, 767, 1, 15]
    >>> B = radix_sort(A)
    >>> B
    [1, 6, 10, 15, 24, 44, 76, 123, 234, 345, 357, 555, 567, 678, 767]

    """
    max_ = max(A)

    # use a stable sort to sort array A on digit i
    exp = 1
    while max_ // exp > 0:
        B = [None] * len(A)
        _counting_sort(A, B, exp)
        A, B = B, A
        exp *= 10
        # print(A)
    return B


def _counting_sort(A, B, exp):
    """
    COUNTING-SORT algorithm for radix sort subroutine.

    The stable sort used as the intermediate sorting algorithm.
    """
    n = len(A)
    C = [0] * 10
    for j in range(n):
        C[(A[j] // exp) % 10] += 1
    # C[i] now contains the number of elements equal to i.
    for i in range(1, 10):
        C[i] += C[i - 1]
    # C[i] now contains the number of elements less than or equal to i.
    for j in range(n-1, -1, -1):
        # if reverse:
        #     B[n - C[(A[j] // exp) % 10]] = A[j]
        # else:
        B[C[(A[j] // exp) % 10] - 1] = A[j]
        C[(A[j] // exp) % 10] -= 1
