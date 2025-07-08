
# from ..exceptions import QueueUnderflowError, QueueOverflowError
from exceptions import QueueUnderflowError, QueueOverflowError
from ._linked_list import SinglyLinkedList
# from ..utils import (
#     ReadOnly,
# )
from utils import ReadOnly

__all__ = ["Queue", "Deque", "SinglyLinkedListQueue"]


class Queue:
    """
    An array implementation of Queue.

    The element dequeued is always the one at
    the head of the queue: the stack implements a fast-in, first-out,
    or FIFO, policy.

    Parameters
    ----------
    n : int
        A queue of at most n elements with an array Q[1..n].

    head : int, default=0
        Initial head of the queue. If not 0 then queue starts in the middle.

    Attributes
    ----------
    Q : list
        A queue of at most n elements with an array Q[1..n].

    head : int
        Q.head that indexes, or points to, its head.

    tail : int
        Q.tail indexes the next location at which a newly arriving
        element will be inserted into the queue.

    Notes
    -----
    The elements in the queue reside in
    locations Q.head,Q.head+1,...,Q:tail-1, where queue “wrap around” in the
    sense that location 1 immediately follows location n in a circular order.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> q = Queue(12, 6)
    >>> q.enqueue(15)
    >>> q.enqueue(6)
    >>> q.enqueue(9)
    >>> q.enqueue(8)
    >>> q.enqueue(4)
    >>> q.enqueue(17)
    >>> q.enqueue(3)
    >>> q.enqueue(5)
    >>> q.Q
    [3, 5, None, None, None, None, 15, 6, 9, 8, 4, 17]
    >>> q.dequeue()
    15
    >>> len(q)
    7
    >>> q.queue_empty()
    False

    Another example in CLRS Exercises 10.1-1
    >>> q = Queue(6)
    >>> q.enqueue(4)
    >>> q.enqueue(1)
    >>> q.enqueue(3)
    >>> q.dequeue()
    >>> q.enqueue(8)
    >>> q.dequeue()
    >>> q.Q
    [4, 1, 3, 8, None, None]
    >>> q.head
    2

    """

    Q = ReadOnly()
    n = ReadOnly()
    head = ReadOnly()
    tail = ReadOnly()

    def __init__(self, n, head=0):
        self._Q = [None] * n
        self._n = n
        self._head = head
        self._tail = head

    def __str__(self):
        # TODO: pretty print of stack elements. Better representation
        return str(self._Q)

    def __len__(self):
        if self._tail >= self._head:
            return self._tail - self._head
        else:
            return self._tail + (self._n - self._head)

    def queue_empty(self):
        """Test to see whether the queue is empty."""
        if self._head == self._tail:
            return True
        return False

    def enqueue(self, x):
        """
        The INSERT operation on a queue

        Parameters
        ----------
        x : int
            The element to be inserted.

        """
        if self._head == (self._tail + 1) % self._n:
            raise QueueOverflowError("Queue overflows.")
        self._Q[self._tail] = x
        if self._tail == self._n - 1:
            self._tail = 0
        else:
            self._tail += 1

    def dequeue(self):
        """
        The DELETE operation on a queue.

        Returns
        -------
        top : int
            The top element to be dequeued.

        """
        if self.queue_empty():
            raise QueueUnderflowError("Queue underflows.")
        x = self._Q[self._head]
        if self._head == self._n:
            self._head = 0
        else:
            self._head += 1
        return x


class Deque(Queue):
    """
    Deque (double-ended queue)

    allows insertion and deletion at both ends.

    Parameters
    ----------
    n : int
        A queue of at most n elements with an array Q[1..n].

    head : int, default=0
        Initial head of the queue. If not 0 then queue starts in the middle.

    Attributes
    ----------
    Q : list
        A queue of at most n elements with an array Q[1..n].

    head : int
        Q.head that indexes, or points to, its head.

    tail : int
        Q.tail indexes the next location at which a newly arriving
        element will be inserted into the queue.

    Notes
    -----
    The elements in the queue reside in
    locations Q.head,Q.head+1,...,Q:tail-1, where queue “wrap around” in the
    sense that location 1 immediately follows location n in a circular order.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> q = Deque(12, 6)
    >>> q.enqueue(15)
    >>> q.enqueue(6)
    >>> q.enqueue(9)
    >>> q.enqueue(8)
    >>> q.enqueue(4)
    >>> q.enqueue(17)
    >>> q.enqueue(3)
    >>> q.enqueue(5)
    >>> q.Q
    [3, 5, None, None, None, None, 15, 6, 9, 8, 4, 17]

    Insertion at head end

    >>> q.head_enqueue(14)
    >>> q.Q
    [3, 5, None, None, None, 14, 15, 6, 9, 8, 4, 17]

    Deletion at tail end
    >>> q.tail_dequeue()
    5

    """
    
    def __init__(self, n, head=0):
        super().__init__(n, head)

    def head_enqueue(self, x):
        """
        The INSERT operation on a queue from head side.

        Parameters
        ----------
        x : int
            The element to be inserted.

        """
        if self._head == (self._tail + 1) % self._n:
            raise QueueOverflowError("Queue overflows.")
        self._Q[(self._head - 1) % self._n] = x
        if self._head == 0:
            self._head = self._n - 1
        else:
            self._head -= 1

    def tail_dequeue(self):
        """
        The DELETE operation on a queue from tail side.

        Returns
        -------
        top : int
            The top element to be dequeued.

        """
        if self.queue_empty():
            raise QueueUnderflowError("Queue underflows.")
        x = self._Q[(self._tail - 1) % self._n]
        if self._tail == 0:
            self._tail = self._n - 1
        else:
            self._tail -= 1
        return x


class SinglyLinkedListQueue:
    """
    An implementation of Queue using singly linked list.

    The element dequeued is always the one at
    the head of the queue: the stack implements a fast-in, first-out,
    or FIFO, policy.

    TODO: implement SinglyLinkedListQueue. Exercises 10.2-3

    Parameters
    ----------
    n : int
        A queue of at most n elements with an array Q[1..n].

    head : int, default=0
        Initial head of the queue. If not 0 then queue starts in the middle.

    Attributes
    ----------
    Q : list
        A queue of at most n elements with an array Q[1..n].

    head : int
        Q.head that indexes, or points to, its head.

    tail : int
        Q.tail indexes the next location at which a newly arriving
        element will be inserted into the queue.

    Notes
    -----
    The elements in the queue reside in
    locations Q.head,Q.head+1,...,Q:tail-1, where queue “wrap around” in the
    sense that location 1 immediately follows location n in a circular order.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> q = SinglyLinkedListQueue(12, 6)
    >>> q.enqueue(15)
    >>> q.enqueue(6)
    >>> q.enqueue(9)
    >>> q.enqueue(8)
    >>> q.enqueue(4)
    >>> q.enqueue(17)
    >>> q.enqueue(3)
    >>> q.enqueue(5)
    >>> q.Q
    [3, 5, None, None, None, None, 15, 6, 9, 8, 4, 17]
    >>> q.dequeue()
    15
    >>> len(q)
    7
    >>> q.queue_empty()
    False

    Another example in CLRS Exercises 10.1-1
    >>> q = Queue(6)
    >>> q.enqueue(4)
    >>> q.enqueue(1)
    >>> q.enqueue(3)
    >>> q.dequeue()
    >>> q.enqueue(8)
    >>> q.dequeue()
    >>> q.Q
    [4, 1, 3, 8, None, None]
    >>> q.head
    2

    """

    Q = ReadOnly()
    n = ReadOnly()
    head = ReadOnly()
    tail = ReadOnly()

    def __init__(self, n, head=0):
        self._Q = SinglyLinkedList()
        self._n = n
        self._head = head
        self._tail = head

    def __str__(self):
        # TODO: pretty print of stack elements. Better representation, after print SLL
        # return str(self._Q)
        pass

    def __len__(self):
        if self._tail >= self._head:
            return self._tail - self._head
        else:
            return self._tail + (self._n - self._head)

    def queue_empty(self):
        """Test to see whether the queue is empty."""
        if self._head == self._tail:
            return True
        return False

    def enqueue(self, x):
        """
        The INSERT operation on a queue

        Parameters
        ----------
        x : int
            The element to be inserted.

        """
        if self._head == (self._tail + 1) % self._n:
            raise QueueOverflowError("Queue overflows.")
        if self.queue_empty():
            self._Q._head = self._Q.element(x)
        else:
            e = self._Q._head
            # while e.next is not None:
            #     e = e.next
            for _ in range(self._tail - self._head):
                e = e.next
            e.next = self._Q.element(x)
        # self._Q[self._tail] = x
        if self._tail == self._n - 1:
            self._tail = 0
        else:
            self._tail += 1

    def dequeue(self):
        """
        The DELETE operation on a queue.

        Returns
        -------
        top : int
            The top element to be dequeued.

        """
        if self.queue_empty():
            raise QueueUnderflowError("Queue underflows.")
        e = self._Q._head
        self._Q.list_delete(e.key)
        # x = self._Q[self._head]
        if self._head == self._n:
            self._head = 0
        else:
            self._head += 1
        return e.key
