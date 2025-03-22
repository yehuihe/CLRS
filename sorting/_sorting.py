import math
from operator import ge, le
from random import randrange


__all__ = ["bubble_sort", "insertion_sort", "selection_sort",
           "merge", "merge_sort", "MaxHeap", "MinHeap", "heap_sort",
           "partition", "quicksort", "randomized_partition",
           "randomized_quicksort", "hoare_partition", "hoare_quicksort",
           "counting_sort"]


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


def _parent(i):
    """
    Indices of heap parent.

    Parameters
    ----------
    i : int
        Given the index i of a node

    Returns
    -------
    parent : int
        Indices of heap parent

    Notes
    -----
    parent node : math.floor(i / 2)

    """
    return i >> 1


def _left(i):
    """
    Indices of heap left child.

    Parameters
    ----------
    i : int
        Given the index i of a node

    Returns
    -------
    left_child : int
        Indices of heap left child

    Notes
    -----
    left child node : 2 * i

    """
    return i << 1


def _right(i):
    """
    Indices of heap right child.

    Parameters
    ----------
    i : int
        Given the index i of a node

    Returns
    -------
    right_child : int
        Indices of heap right child

    Notes
    -----
    right child node : 2 * i + 1

    """
    return (i << 1) + 1


def max_heapify(A, i):
    """
    MAX-HEAPIFY procedure.

    In order to maintain the max-heap property.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.
    i : int
        Given the index i of a node. IMPORTANT: i is in python convention 0 index-based.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an')
        in order to maintain the max-heap property

        A[PARENT(i)] >= A[i]

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the max-heapify algorithm is:

    >>> A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    >>> max_heapify(A, 1)
    >>> A
    [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    >>> A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    >>> max_heapify(A, 2)
    >>> A
    [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]

    """
    # if heap_size > len(A):
    #     raise ValueError("Heap size {} is larger than length of A".format(heap_size))
    heap_size = len(A)

    l = _left(i+1)
    r = _right(i+1)
    if l <= heap_size and A[l-1] > A[i]:
        largest = l - 1
    else:
        largest = i
    if r <= heap_size and A[r-1] > A[largest]:
        largest = r - 1
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def max_heapify_iterative(A, i):
    """
    MAX-HEAPIFY iterative procedure.

    In order to maintain the max-heap property.

    For documentation for the rest of the parameters, see ref:`(see here) <sorting.max_heapify>`

    """
    # if heap_size > len(A):
    #     raise ValueError("Heap size {} is larger than length of A".format(heap_size))
    heap_size = len(A)

    while True:
        l = _left(i+1)
        r = _right(i+1)
        if l <= heap_size and A[l-1] > A[i]:
            largest = l - 1
        else:
            largest = i
        if r <= heap_size and A[r-1] > A[largest]:
            largest = r - 1
        if largest == i:
            break
        A[i], A[largest] = A[largest], A[i]
        i = largest


def min_heapify(A, i):
    """
    MIN-HEAPIFY procedure.

    In order to maintain the min-heap property.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.
    i : int
        Given the index i of a node. IMPORTANT: i is in python convention 0 index-based.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an')
        in order to maintain the min-heap property.

        A[PARENT(i)] <= A[i]

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the min-heapify algorithm is:

    >>> A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    >>> min_heapify(A, 3)
    >>> A
    [16, 4, 10, 2, 7, 9, 3, 14, 8, 1]

    """
    # if heap_size > len(A):
    #     raise ValueError("Heap size {} is larger than length of A".format(heap_size))
    heap_size = len(A)

    l = _left(i+1)
    r = _right(i+1)
    if l <= heap_size and A[l-1] < A[i]:
        smallest = l - 1
    else:
        smallest = i
    if r <= heap_size and A[r-1] < A[smallest]:
        smallest = r - 1
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def min_heapify_iterative(A, i):
    """
    MIN-HEAPIFY iterative procedure.

    In order to maintain the min-heap property.

    For documentation for the rest of the parameters, see ref:`(see here) <sorting.min_heapify>`

    """
    # if heap_size > len(A):
    #     raise ValueError("Heap size {} is larger than length of A".format(heap_size))
    # if heap_size > len(A):
    #     raise ValueError("Heap size {} is larger than length of A".format(heap_size))
    heap_size = len(A)

    while True:
        l = _left(i+1)
        r = _right(i+1)
        if l <= heap_size and A[l-1] < A[i]:
            smallest = l - 1
        else:
            smallest = i
        if r <= heap_size and A[r-1] < A[smallest]:
            smallest = r - 1
        if smallest == i:
            break
        A[i], A[smallest] = A[smallest], A[i]
        i = smallest


def build_max_heap(A):
    """
    BUILD-MAX-HEAP procedure.

    Building a max-heap

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an')
        produces a max-heap.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the build max heap algorithm is:

    >>> A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    >>> build_max_heap(A)
    >>> A
    [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    >>> A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    >>> build_max_heap(A)
    >>> A
    [84, 22, 19, 10, 3, 17, 6, 5, 9]

    """
    heap_size = len(A)
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i)


def build_min_heap(A):
    """
    BUILD-MIN-HEAP procedure.

    Building a min-heap

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    A : ndarray, shape (n,)
        A permutation (reordering) of the input sequence (a1', a2', ..., an')
        produces a min-heap.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the build max heap algorithm is:

    >>> A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    >>> build_min_heap(A)
    >>> A
    [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]

    >>> A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    >>> build_min_heap(A)
    >>> A
    [3, 5, 6, 9, 84, 19, 17, 22, 10]

    """
    heap_size = len(A)
    for i in range(len(A) // 2 - 1, -1, -1):
        min_heapify(A, i)


class BaseHeap:
    def __init__(self, A, heap_size):
        self.A = A
        self._heap_size = heap_size
        self._validate_heap_size_constraint()
        # TODO: display the heap based on heap_size
        # TODO: remove this validator from __init__. Setter has validator

    def __len__(self):
        return len(self.A)

    def __iadd__(self, other):
        self._validate_heap_size_constraint()
        self._heap_size += other
        return self

    def __isub__(self, other):
        self._validate_heap_size_constraint()
        self._heap_size -= other
        return self

    @property
    def heap_size(self):
        return self._heap_size

    @heap_size.setter
    def heap_size(self, value):
        self._validate_heap_size_constraint()
        self._heap_size = value

    def _validate_heap_size_constraint(self):
        if self.heap_size < 0 or self.heap_size > len(self):
            raise ValueError(f"Heap size {self.heap_size} cannot be greater than length {len(self)}.")

    @staticmethod
    def _parent(i):
        """
        Indices of heap parent.

        Parameters
        ----------
        i : int
            Given the index i of a node

        Returns
        -------
        parent : int
            Indices of heap parent

        Notes
        -----
        parent node : math.floor(i / 2)

        """
        return i >> 1

    @staticmethod
    def _left(i):
        """
        Indices of heap left child.

        Parameters
        ----------
        i : int
            Given the index i of a node

        Returns
        -------
        left_child : int
            Indices of heap left child

        Notes
        -----
        left child node : 2 * i

        """
        return i << 1

    @staticmethod
    def _right(i):
        """
        Indices of heap right child.

        Parameters
        ----------
        i : int
            Given the index i of a node

        Returns
        -------
        right_child : int
            Indices of heap right child

        Notes
        -----
        right child node : 2 * i + 1

        """
        return (i << 1) + 1


class MaxHeap(BaseHeap):
    """
    The (binary) max-heap data structure.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    heap_size : int
        A.heap-size, which represents how many elements in the
        heap are stored within array A.

    Notes
    -----
    A[1..A.length] may contain numbers, only the elements in A[1::A.heap_size],
    where 0 <= A.heap-size <= A.length, are valid elements of the heap.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    # TODO: write example
    A simple application of the insertion sort algorithm is:

    """

    def max_heapify(self, i):
        """
        MAX-HEAPIFY procedure.

        In order to maintain the max-heap property.

        Parameters
        ----------
        i : int
            Given the index i of a node. IMPORTANT: i is in python convention 0 index-based.

        Returns
        -------
        A : ndarray, shape (n,)
            A permutation (reordering) of the input sequence (a1', a2', ..., an')
            in order to maintain the max-heap property

            A[PARENT(i)] >= A[i]

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the max-heapify algorithm is:

        >>> A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        >>> max_heap = MaxHeap(A, 10)
        >>> max_heap.max_heapify(1)
        >>> max_heap.A
        [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

        >>> A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
        >>> max_heap = MaxHeap(A, 14)
        >>> max_heap.max_heapify(2)
        >>> max_heap.A
        [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]

        """
        l = self._left(i + 1)
        r = self._right(i + 1)
        if l <= self._heap_size and self.A[l - 1] > self.A[i]:
            largest = l - 1
        else:
            largest = i
        if r <= self._heap_size and self.A[r - 1] > self.A[largest]:
            largest = r - 1
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def max_heapify_iterative(self, i):
        """
        MAX-HEAPIFY iterative procedure.

        In order to maintain the max-heap property.

        For documentation for the rest of the parameters, see ref:`(see here) <sorting.max_heapify>`

        """
        while True:
            l = self._left(i + 1)
            r = self._right(i + 1)
            if l <= self._heap_size and self.A[l - 1] > self.A[i]:
                largest = l - 1
            else:
                largest = i
            if r <= self._heap_size and self.A[r - 1] > self.A[largest]:
                largest = r - 1
            if largest == i:
                break
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            i = largest

    def build_max_heap(self):
        """
        BUILD-MAX-HEAP procedure.

        Building a max-heap

        Returns
        -------
        A : ndarray, shape (n,)
            A permutation (reordering) of the input sequence (a1', a2', ..., an')
            produces a max-heap.

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the build max heap algorithm is:

        >>> A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        >>> max_heap = MaxHeap(A, 10)
        >>> max_heap.build_max_heap()
        >>> max_heap.A
        [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

        >>> A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
        >>> max_heap = MaxHeap(A, 10).build_max_heap()
        >>> max_heap.A
        [84, 22, 19, 10, 3, 17, 6, 5, 9]

        """
        self._heap_size = len(self)
        for i in range(len(self) // 2 - 1, -1, -1):
            self.max_heapify(i)

        return self

    def heap_maximum(self):
        """
        HEAP-MAXIMUM procedure.

        Returns the element of A with the largest key

        Returns
        -------
        max : int
            Element of a with the largest key.

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        """
        return self.A[0]

    def heap_extract_max(self):
        """
        HEAP-EXTRACT-MAX procedure.

        TODO: fix heap-size display
        TODO: raise custom Error instead of ValueError

        Removes and returns the element of A with the largest key.

        Returns
        -------
        max : int
            The element of A with the largest key

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        >>> max_heap = MaxHeap(A, 12)
        >>> max = max_heap.heap_extract_max()
        >>> max
        15
        >>> max_heap.heap_size
        11
        >>> max_heap.A
        [13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2, 1]

        """
        if self.heap_size < 1:
            raise ValueError("Heap underflow.")
        max = self.A[0]
        self.A[0] = self.A[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i, key):
        """
        HEAP-INCREASE-KEY procedure.

        TODO: fix heap-size display
        TODO: raise custom Error instead of ValueError

        The procedure HEAP-INCREASE-KEY implements the INCREASE-KEY operation.

        Parameters
        ----------
        i : int
            An index i into the array identifies the priority-queue element whose key we
            wish to increase

        key : int
            New value key. Assumed to be at least as large as i’s current key value

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        >>> max_heap = MaxHeap(A, 10).heap_increase_key(8, 15)
        >>> max_heap.heap_size
        11
        >>> max_heap.A
        [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

        """
        if key < self.A[i]:
            raise ValueError(f"new key {key} is smaller than current key {self.A[i]}.")
        self.A[i] = key
        while i > 0 and self.A[self._parent(i+1)-1] < self.A[i]:
            # print(self.A, i)
            self.A[i], self.A[self._parent(i+1)-1] = self.A[self._parent(i+1)-1], self.A[i]
            i = self._parent(i+1) - 1

        return self

    def max_heap_insert(self, key):
        """
        MAX-HEAP-INSERT procedure.

        Inserts the element key into the heap A

        Parameters
        ----------
        key : int
            It takes as an input the key of the new element to be inserted into max-heap A

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        >>> max_heap = MaxHeap(A, 12).max_heap_insert(10)
        >>> max_heap.heap_size
        13
        >>> max_heap.A
        [15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8]

        """
        self.heap_size += 1
        self.A.append(-math.inf)
        self.heap_increase_key(self.heap_size-1, key)

        return self


class MinHeap(BaseHeap):
    """
    The (binary) min-heap data structure.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    heap_size : int
        A.heap-size, which represents how many elements in the
        heap are stored within array A.

    Notes
    -----
    A[1..A.length] may contain numbers, only the elements in A[1::A.heap_size],
    where 0 <= A.heap-size <= A.length, are valid elements of the heap.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    # TODO: write example
    A simple application of the insertion sort algorithm is:

    """

    def min_heapify(self, i):
        """
        MIN-HEAPIFY procedure.

        In order to maintain the min-heap property.

        Parameters
        ----------
        i : int
            Given the index i of a node. IMPORTANT: i is in python convention 0 index-based.

        Returns
        -------
        A : ndarray, shape (n,)
            A permutation (reordering) of the input sequence (a1', a2', ..., an')
            in order to maintain the min-heap property.

            A[PARENT(i)] <= A[i]

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the min-heapify algorithm is:

        >>> A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        >>> min_heap = MinHeap(A, 10)
        >>> min_heap.min_heapify(3)
        >>> min_heap.A
        [16, 4, 10, 2, 7, 9, 3, 14, 8, 1]

        """
        l = self._left(i + 1)
        r = self._right(i + 1)
        if l <= self._heap_size and self.A[l - 1] < self.A[i]:
            smallest = l - 1
        else:
            smallest = i
        if r <= self._heap_size and self.A[r - 1] < self.A[smallest]:
            smallest = r - 1
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.min_heapify(smallest)

    def min_heapify_iterative(self, i):
        """
        MIN-HEAPIFY iterative procedure.

        In order to maintain the min-heap property.

        For documentation for the rest of the parameters, see ref:`(see here) <sorting.min_heapify>`

        """
        while True:
            l = self._left(i + 1)
            r = self._right(i + 1)
            if l <= self._heap_size and self.A[l - 1] < self.A[i]:
                smallest = l - 1
            else:
                smallest = i
            if r <= self._heap_size and self.A[r - 1] < self.A[smallest]:
                smallest = r - 1
            if smallest == i:
                break
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            i = smallest

    def build_min_heap(self):
        """
        BUILD-MIN-HEAP procedure.

        Building a min-heap

        Returns
        -------
        A : ndarray, shape (n,)
            A permutation (reordering) of the input sequence (a1', a2', ..., an')
            produces a min-heap.

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the build max heap algorithm is:

        >>> A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        >>> min_heap = MinHeap(A, 10)
        >>> min_heap.build_min_heap()
        >>> min_heap.A
        [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]

        >>> A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
        >>> min_heap = MinHeap(A, 10)
        >>> min_heap.build_min_heap()
        >>> min_heap.A
        [3, 5, 6, 9, 84, 19, 17, 22, 10]

        """
        self._heap_size = len(self)
        for i in range(len(self) // 2 - 1, -1, -1):
            self.min_heapify(i)


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
    max_heap = MaxHeap(A, len(A)).build_max_heap()
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heap.heap_size -= 1
        max_heap.max_heapify(0)
        # print(A)


class MaxPriorityQueue(MaxHeap):
    def __init__(self, S):
        super().__init__(S, len(S))

    def insert(self, x):
        """
        INSERT procedure.

        Inserts the element x into the set S, which is equivalent to the operation
        S = S \cup {x}.

        Parameters
        ----------
        key : int
            It takes as an input the key of the new element to be inserted into max-heap A

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> S = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        >>> mpq = MaxPriorityQueue(S).insert(10)
        >>> max_heap.heap_size
        13
        >>> max_heap.A
        [15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8]

        """
        super().max_heap_insert(x)

    def maximum(self):
        """
        MAXIMUM procedure.

        returns the element of S with the largest key.

        Returns
        -------
        max : int
            Element of S with the largest key.

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        """
        return super().heap_maximum()

    def extract_max(self):
        """
        EXTRACT-MAX procedure.

        Removes and returns the element of S with the largest key.

        Returns
        -------
        max : int
            The element of A with the largest key

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> S = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        >>> mpq = MaxPriorityQueue(S)
        >>> max = mpq.heap_extract_max()
        >>> max
        15
        >>> mpq.heap_size
        11
        >>> mpq.A
        [13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2, 1]

        """
        return super().heap_extract_max()

    def increase_key(self, x, k):
        """
        INCREASE-KEY procedure.

        Increases the value of element x’s key to the new value k,
        which is assumed to be at least as large as x’s current key value.

        Parameters
        ----------
        x : int
            An index x into the array identifies the priority-queue element whose key we
            wish to increase

        k : int
            New value key. Assumed to be at least as large as x’s current key value

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        Examples
        --------
        A simple application of the heap extract max algorithm is:

        >>> S = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        >>> mpq = MaxPriorityQueue(S).heap_increase_key(8, 15)
        >>> mpq.heap_size
        11
        >>> mpq.A
        [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

        """
        super().heap_increase_key(x, k)


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

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

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


def radix_sort(A, d):
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

    reverse : bool, default False
        The reverse flag can be set to sort in descending order.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the counting sort algorithm is:

    >>> A = [329, 457, 657, 839, 436, 720, 355]
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
    B = [None] * len(A)
    for i in range(d):
        counting_sort(A, B, 9)


def radix_sort(A, B, b, r):

    n = len(A)
    for k in range(b // r):
        C = [0] * (1 << r)
        for j in range(n):
            binary = (A[j] >> r * k) & ((1 << r) - 1)
            C[binary] += 1
        for i in range(1, 1 << r):
            C[i] += C[i - 1]
        for j in range(n - 1, -1, -1):
            binary = (A[j] >> r * k) & ((1 << r) - 1)
            C[binary] -= 1
            B[C[binary]] = A[j]
        A = B
    return B

