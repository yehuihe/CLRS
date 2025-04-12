import math

# from ..exceptions import StackUnderflowError, StackOverflowError
from exceptions import HeapUnderflowError
# from ..utils import (
#     ReadOnly,
# )
from utils import ReadOnly

__all__ = ["MaxHeap", "MinHeap"]



class BaseHeap:
    """
    Base class for all (binary) heap data structures.

    Warning: This class should not be used directly. Use derived classes
    instead.

    Parameters
    ----------
    heap_size : int
         Represents how many elements in the heap are stored within
         array A.

    Attributes
    ----------
    A : list
         An array A that represents a heap.

    length : int
        A.length which (as usual) gives the number of elements in the array.
        Access via len(A).

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    """

    A = ReadOnly()
    heap_size = ReadOnly()

    def __init__(self, A, heap_size):
        self._A = A
        self._heap_size = heap_size
        self._validate_heap_size_constraint()
        # TODO: display the heap based on heap_size
        # TODO: remove this validator from __init__. Setter has validator

    def __len__(self):
        return len(self._A)

    def __iadd__(self, other):
        self._validate_heap_size_constraint()
        self._heap_size += other
        return self

    def __isub__(self, other):
        self._validate_heap_size_constraint()
        self._heap_size -= other
        return self

    # @property
    # def heap_size(self):
    #     return self._heap_size
    #
    # @heap_size.setter
    # def heap_size(self, value):
    #     self._validate_heap_size_constraint()
    #     self._heap_size = value

    def _validate_heap_size_constraint(self):
        if self._heap_size < 0 or self._heap_size > len(self):
            raise ValueError(f"Heap size {self._heap_size} cannot be greater than length {len(self)}.")

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
        if l <= self._heap_size and self._A[l - 1] > self._A[i]:
            largest = l - 1
        else:
            largest = i
        if r <= self._heap_size and self._A[r - 1] > self._A[largest]:
            largest = r - 1
        if largest != i:
            self._A[i], self._A[largest] = self._A[largest], self._A[i]
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
            if l <= self._heap_size and self._A[l - 1] > self._A[i]:
                largest = l - 1
            else:
                largest = i
            if r <= self._heap_size and self._A[r - 1] > self._A[largest]:
                largest = r - 1
            if largest == i:
                break
            self._A[i], self._A[largest] = self._A[largest], self._A[i]
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
        return self._A[0]

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
        if self._heap_size < 1:
            raise HeapUnderflowError("Heap underflow.")
        max = self._A[0]
        self._A[0] = self._A[self._heap_size-1]
        self._heap_size -= 1
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
        >>> max_heap = MaxHeap(A, 10)
        >>> max_heap.heap_increase_key(8, 15)
        >>> max_heap.heap_size
        10
        >>> max_heap.A
        [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

        """
        if key < self._A[i]:
            raise ValueError(f"new key {key} is smaller than current key {self._A[i]}.")
        self._A[i] = key
        while i > 0 and self._A[self._parent(i+1)-1] < self._A[i]:
            # print(self._A, i)
            self._A[i], self._A[self._parent(i+1)-1] = self._A[self._parent(i+1)-1], self._A[i]
            i = self._parent(i+1) - 1

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
        >>> max_heap = MaxHeap(A, 12)
        >>> max_heap.max_heap_insert(10)
        >>> max_heap.heap_size
        13
        >>> max_heap.A
        [15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8]

        """
        self._heap_size += 1
        self._A.append(-math.inf)
        self.heap_increase_key(self._heap_size-1, key)


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
        if l <= self._heap_size and self._A[l - 1] < self._A[i]:
            smallest = l - 1
        else:
            smallest = i
        if r <= self._heap_size and self._A[r - 1] < self._A[smallest]:
            smallest = r - 1
        if smallest != i:
            self._A[i], self._A[smallest] = self._A[smallest], self._A[i]
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
            if l <= self._heap_size and self._A[l - 1] < self._A[i]:
                smallest = l - 1
            else:
                smallest = i
            if r <= self._heap_size and self._A[r - 1] < self._A[smallest]:
                smallest = r - 1
            if smallest == i:
                break
            self._A[i], self._A[smallest] = self._A[smallest], self._A[i]
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
