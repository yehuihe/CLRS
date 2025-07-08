import math

# from ..exceptions import StackUnderflowError, StackOverflowError
from exceptions import StackUnderflowError, StackOverflowError
from ._linked_list import SinglyLinkedList
# from ..utils import (
#     ReadOnly,
# )
from utils import ReadOnly

__all__ = ["Stack", "SinglyLinkedListStack"]


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

    Another example in CLRS Exercises 10.1-1
    >>> s = Stack(6)
    >>> s.push(4)
    >>> s.push(1)
    >>> s.push(3)
    >>> s.pop()
    >>> s.push(8)
    >>> s.pop()
    >>> s.S
    [4, 1, 8, None, None, None]
    >>> s.top
    1

    """

    S = ReadOnly()
    n = ReadOnly()
    top = ReadOnly()

    def __init__(self, n):
        self._S = [None] * n
        self._n = n
        self._top = -1

    def __str__(self):
        # TODO: pretty print of stack elements
        return str(self._S[:self._top + 1])

    def __len__(self):
        return self._top + 1

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
        x : object
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
        top : object
            The top element to be popped.

        """
        if self.stack_empty():
            raise StackUnderflowError("Stack underflows.")
        self._top -= 1
        return self._S[self._top + 1]


class SinglyLinkedListStack:
    """
    An implementation of Stack using singly linked list.

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

    Notes
    -----
    CLRS Exercises 10.2-2.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> s = SinglyLinkedListStack(7)
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

    Another example in CLRS Exercises 10.1-1
    >>> s = SinglyLinkedListStack(6)
    >>> s.push(4)
    >>> s.push(1)
    >>> s.push(3)
    >>> s.pop()
    3
    >>> s.push(8)
    >>> s.pop()
    8
    >>> s.S
    [4, 1, 8, None, None, None]
    >>> s.top
    1

    """

    S = ReadOnly()
    n = ReadOnly()
    top = ReadOnly()

    def __init__(self, n):
        self._S = SinglyLinkedList()
        self._n = n
        self._top = -1

    def __str__(self):
        # TODO: pretty print of stack elements, after print SLL
        # return str(self._S[:self._top + 1])
        pass

    def __len__(self):
        return self._top + 1

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
        # self._top += 1
        # self._S[self._top] = x
        if self.stack_empty():
            self._S._head = self._S.element(x)
        else:
            e = self._S._head
            # while e.next is not None:
            #     e = e.next
            for _ in range(self._top):
                e = e.next
            e.next = self._S.element(x)
        self._top += 1

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
        e = self._S._head
        # while e.next is not None:
        #     e = e.next
        for _ in range(self._top):
            e = e.next
        self._S.list_delete(e.key)
        self._top -= 1
        return e.key


