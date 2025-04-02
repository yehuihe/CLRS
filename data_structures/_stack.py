import math

# from ..exceptions import StackUnderflowError, StackOverflowError
from exceptions import StackUnderflowError, StackOverflowError
# from ..utils import (
#     ReadOnly,
# )
from utils import ReadOnly

__all__ = ["Stack", "MaxHeap", "MinHeap"]


# class ReadOnly:
#     """Generic Read-only descriptor for class attributes."""
#
#     def __init__(self):
#         self._name = None
#
#     def __set_name__(self, owner, name):
#         self.name = name
#         self._name = "_" + name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__[self._name]
#
#     def __set__(self, instance, value):
#         if self._name in instance.__dict__:
#             raise AttributeError(f"Can't set attribute {self.name!r}")
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         raise AttributeError(f"Can't delete attribute {self._name!r}")


class Stack:
    """
    An array implementation of Stack.

    The element deleted from the set is the one most
    recently inserted: the stack implements a last-in, first-out,
    or LIFO, policy.

    Parameters
    ----------
    n : int
        A stack of at most n elements with an array S[1..n].

    Attributes
    ----------
    S : list
        A stack of at most n elements with an array S[1..n].

    top : int
        S.top that indexes the most recently inserted element.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> s = Stack(7)
    >>> s.n
    7
    >>> s.push(15)
    >>> s.push(6)
    >>> s.push(2)
    >>> s.push(9)
    >>> s.push(17)
    >>> s.push(3)
    >>> s.S
    [15, 6, 2, 9, 17, 3, None]
    >>> s.pop()
    3
    >>> s.top
    4

    The stack consists of elements S[1..S.top], which can be printed

    >>> print(s)
    [15, 6, 2, 9, 17]
    >>> len(s)
    5
    >>> s.stack_empty()
    False

    """

    S = ReadOnly()
    n = ReadOnly()
    top = ReadOnly()

    def __init__(self, n):
        self._S = [None] * n
        self._n = n
        self._top = -1  # python offset 1

    def __str__(self):
        # TODO: pretty print of stack elements
        return str(self._S[:self._top + 1])

    def __len__(self):
        return self._top + 1

    # Refactored properties to descriptor.
    # @property
    # def n(self):
    #     return self._n
    #
    # @property
    # def top(self):
    #     return self._top

    def stack_empty(self):
        """Test to see whether the stack is empty."""
        if self._top == -1:
            return True
        return False

    def push(self, x):
        """
        The INSERT operation on a stack

        Parameters
        ----------
        x : int
            The element to be inserted.

        """
        if self._top + 1 >= self._n:
            raise StackOverflowError("Stack overflows.")
        self._top += 1
        self._S[self._top] = x

    def pop(self):
        """
        The DELETE operation on a stack.

        Returns
        -------
        top : int
            The top element to be popped.

        """
        if self.stack_empty():
            raise StackUnderflowError("Stack underflows.")
        self._top -= 1
        return self._S[self._top + 1]


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
