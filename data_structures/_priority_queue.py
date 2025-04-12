from ._heap import MaxHeap


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
        >>> mpq = MaxPriorityQueue(S)
        >>> mpq.insert(10)
        >>> mpq.heap_size
        13
        >>> mpq.A
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
        >>> mpq = MaxPriorityQueue(S)
        >>> mpq.heap_increase_key(8, 15)
        >>> mpq.heap_size
        11
        >>> mpq.A
        [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

        """
        super().heap_increase_key(x, k)
