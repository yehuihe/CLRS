from abc import ABCMeta, abstractmethod

# from ..utils import (
#     ReadOnly,
# )
from utils import ReadOnly

__all__ = ["SinglyLinkedList",
           "CircularSinglyLinkedList",
           "DoublyLinkedList",
           "CircularDoublyLinkedList"]

# TODO: implement __getitem__, __setitem__, __delitem__, __len__, __iter__


class BaseLinkedList(metaclass=ABCMeta):
    """Base class for all linked lists in CLRS."""

    @abstractmethod
    def __init__(self):
        pass

    def element(self, k):
        """Generate a element with key k."""
        return self.__class__.Element(k)

    @abstractmethod
    def list_search(self, k):
        """Searching a linked list"""
        pass

    @abstractmethod
    def list_insert(self, x):
        """Inserting into a linked list."""
        pass


class BaseSinglyLinkedList(BaseLinkedList, metaclass=ABCMeta):
    """Base class for singly linked lists."""

    class Element:
        """
        The element of a singly linked list L

        Object with an attribute key and
        one other pointer attribute: next.

        Attributes
        ----------
        key : object, default: None
            The key of this element.

        next : object, default: None
            The next pointer of this element.

        Examples
        --------
        Create an element with key 25:

        >>> x = L.element(25)
        >>> x
        SinglyLinkedList.Element(key=25, address=0x2490300da50)

        """
        __slots__ = ["key", "next"]

        def __init__(self, key):
            self.key = key
            self.next = None

        def __repr__(self):
            return f"{self.__class__.__qualname__}(key={self.key}, address={hex(id(self))})"


class BaseDoublyLinkedList(BaseLinkedList, metaclass=ABCMeta):
    """Base class for doubly linked lists."""

    class Element:
        """
        The element of a doubly linked list L

        An object with an attribute key and two other pointer
         attributes: next and prev.

        Attributes
        ----------
        key : object
            The key of this element.

        next : object, default: None
            The next pointer of this element.

        prev : object, default: None
            The prev pointer of this element.

        Examples
        --------
        Create an element with key 25:

        >>> x = L.element(25)
        >>> x
        DoublyLinkedList.Element(key=25, address=0x2490300da50)

        """
        __slots__ = ["key", "next", "prev"]

        def __init__(self, key):
            self.key = key
            self.next = None
            self.prev = None

        def __repr__(self):
            return f"{self.__class__.__qualname__}(key={self.key}, address={hex(id(self))})"


class SinglyLinkedList(BaseSinglyLinkedList):
    """
    Singly linked list.

    # TODO: implement DELETE
    # TODO: list_delete reference implementation

    Unsorted and doubly linked list.

    Attributes
    ----------
    head : Element, default: None
        An attribute L.head points to the first element of the
        list. If L.head=None, the list is empty.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the singly linked list data structure is:

    >>> L = SinglyLinkedList()
    >>> L.list_insert(L.element(1))
    >>> L.list_insert(L.element(4))
    >>> L.list_insert(L.element(16))
    >>> L.list_insert(L.element(9))
    >>> L.head
    SinglyLinkedList.Element(key=9, address=0x2490300da50)

    Finds the first element with key 16 in list L

    >>> x = L.list_search(16)
    >>> x
    SinglyLinkedList.Element(key=16, address=0x2490300d870)

    Insert an element with key 25 as the new head

    >>> x = L.element(25)
    >>> L.list_insert(x)
    >>> L.head
    SinglyLinkedList.Element(key=25, address=0x25b83325b40)

    TO remove an element x from a linked list L

    >>> L.list_delete(4)
    >>> L.list_search(4)

    """
    head = ReadOnly()

    # This is for the purpose of correct __qualname__ for subclass.
    class Element(BaseSinglyLinkedList.Element):
        pass

    def __init__(self):
        self._head = None

    def __repr__(self):
        return f"{self.Element.__qualname__}(head={repr(self._head)})"

    def list_search(self, k):
        """
        Searching a linked list

        Finds the first element with key k in list L
        by a simple linear search, returning a pointer to this element

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : Element
            The element with key k.

        """
        x = self._head
        while x is not None and x.key != k:
            x = x.next
        return x

    def list_insert(self, x):
        """
        Inserting into a linked list.

        Given an element x whose key attribute has already been set,
        LIST INSERT procedure “splices” x onto
        the front of the linked list.

        Parameters
        ----------
        x : Element
            The element to insert.

        """
        x.next = self._head
        self._head = x

    # def list_delete(self, x):
    #     """
    #     Deleting from a linked list.
    #
    #     The procedure LIST-DELETE Removes an element x from a linked list L.
    #     It must be given a pointer to x, and it then “splices” x
    #     out of the list by updating pointers. If we wish to delete an element
    #     with a given key, we must first call
    #     LIST-SEARCH to retrieve a pointer to the element.
    #
    #     Parameters
    #     ----------
    #     x : Element
    #         The element to delete.
    #
    #     """
    #     if x.prev is not None:
    #         x.prev.next = x.next
    #     else:
    #         self._head = x.next
    #     if x.next is not None:
    #         x.next.prev = x.prev

    def list_delete(self, k):
        """
        Deleting from a linked list.

        The procedure LIST-DELETE Removes an element x from a linked list L.
        It must be given a pointer to x, and it then “splices” x
        out of the list by updating pointers. If we wish to delete an element
        with a given key, we must first call
        LIST-SEARCH to retrieve a pointer to the element.

        Parameters
        ----------
        k : int
            Given key of the element to delete.

        """
        x = self._head
        if x.key == k:
            self._head = self._head.next
        else:
            while x.next is not None and x.next.key != k:
                x = x.next
            x.next = x.next.next


class CircularSinglyLinkedList(BaseSinglyLinkedList):
    """
    Circular singly linked list.

    # TODO: implement DELETE
    # TODO: list_delete reference implementation

    Unsorted and doubly linked list.

    Attributes
    ----------
    head : Element, default: None
        An attribute L.head points to the first element of the
        list. If L.head=None, the list is empty.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the singly linked list data structure is:

    >>> L = CircularSinglyLinkedList()
    >>> L.list_insert(L.element(1))
    >>> L.list_insert(L.element(4))
    >>> L.list_insert(L.element(16))
    >>> L.list_insert(L.element(9))

    Finds the first element with key 16 in list L

    >>> x = L.list_search(16)
    >>> x
    CircularSinglyLinkedList.Element(key=16, address=0x2490300d870)

    Insert an element with key 25 as the new head

    >>> x = L.element(25)
    >>> L.list_insert(x)
    >>> x.next
    CircularSinglyLinkedList.Element(key=9, address=0x169f03a2350)

    To remove an element x from a linked list L

    >>> L.list_delete(1)
    >>> L.list_search(1)
    CircularSinglyLinkedList.Element(key=None, address=0x169f02b9bd0)

    It's the sentinel. L does not contain Element with key=1 anymore.

    """

    # head = ReadOnly()

    # This is for the purpose of correct __qualname__ for subclass.
    class Element(BaseSinglyLinkedList.Element):
        pass

    def __init__(self):
        self._sentinel = self.Element(None)
        self._sentinel.next = self._sentinel

    def list_search(self, k):
        """
        Searching a linked list

        Finds the first element with key k in list L
        by a simple linear search, returning a pointer to this element

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : Element
            The element with key k.

        """
        # self._sentinel.key = k
        x = self._sentinel.next
        while x is not self._sentinel and x.key != k:
            x = x.next
        return x

    def list_insert(self, x):
        """
        Inserting into a linked list.

        Given an element x whose key attribute has already been set,
        LIST INSERT procedure “splices” x onto
        the front of the linked list.

        Parameters
        ----------
        x : Element
            The element to insert.

        """
        x.next = self._sentinel.next
        self._sentinel.next = x

    # def list_delete(self, x):
    #     """
    #     Deleting from a linked list.
    #
    #     The procedure LIST-DELETE Removes an element x from a linked list L.
    #     It must be given a pointer to x, and it then “splices” x
    #     out of the list by updating pointers. If we wish to delete an element
    #     with a given key, we must first call
    #     LIST-SEARCH to retrieve a pointer to the element.
    #
    #     Parameters
    #     ----------
    #     x : Element
    #         The element to delete.
    #
    #     """
    #     if x.prev is not None:
    #         x.prev.next = x.next
    #     else:
    #         self._head = x.next
    #     if x.next is not None:
    #         x.next.prev = x.prev

    def list_delete(self, x=None, k=None):
        """
        Deleting from a linked list.

        TODO: still need to implement delete with pointer

        The procedure LIST-DELETE Removes an element x from a linked list L.
        It must be given a pointer to x, and it then “splices” x
        out of the list by updating pointers. If we wish to delete an element
        with a given key, we must first call
        LIST-SEARCH to retrieve a pointer to the element.

        Parameters
        ----------
        x : DoublyLinkedList.Element
            The element to delete.

        k : int
            Given key of the element to delete.

        """
        x = self._sentinel
        while x.next is not self._sentinel and x.next.key != k:
            x = x.next
        x.next = x.next.next


class DoublyLinkedList(BaseDoublyLinkedList):
    """
    Doubly linked list.

    # TODO: list_delete reference implementation

    Unsorted and doubly linked list.

    Attributes
    ----------
    head : Element, default: None
        An attribute L.head points to the first element of the
        list. If L.head=None, the list is empty.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> L = DoublyLinkedList()

    Use DoublyLinkedList.element(key) to generate an element for doubly linked list

    >>> L.list_insert(L.element(1))
    >>> e = L.element(4)
    >>> L.list_insert(e)
    >>> L.list_insert(L.element(16))
    >>> L.list_insert(L.element(9))
    >>> L.head
    DoublyLinkedList.Element(key=9, address=0x208ea29d300)

    Finds the first element with key 16 in list L

    >>> x = L.list_search(16)
    >>> x
    DoublyLinkedList.Element(key=16, address=0x208ea29c880)

    Insert an element with key 25 as the new head

    >>> x = L.element(25)
    >>> L.list_insert(x)
    >>> L.head
    DoublyLinkedList.Element(key=25, address=0x208ea2b9f40)

    TO remove an element e (key=4, see above) from a linked list L

    >>> L.list_delete(e)
    >>> L.list_search(4)

    """
    head = ReadOnly()

    # This is for the purpose of correct __qualname__ for subclass.
    class Element(BaseDoublyLinkedList.Element):
        pass

    def __init__(self):
        self._head = None

    def __repr__(self):
        return f"{self.Element.__qualname__}(head={repr(self._head)})"

    def list_search(self, k):
        """
        Searching a linked list

        Finds the first element with key k in list L
        by a simple linear search, returning a pointer to this element

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : Element
            The element with key k.

        """
        x = self._head
        while x is not None and x.key != k:
            x = x.next
        return x

    def list_insert(self, x):
        """
        Inserting into a linked list.

        Given an element x whose key attribute has already been set,
        LIST INSERT procedure “splices” x onto
        the front of the linked list.

        Parameters
        ----------
        x : Element
            The element to insert.

        """
        x.next = self._head
        if self._head is not None:
            self._head.prev = x
        self._head = x
        x.prev = None

    def list_delete(self, x=None, k=None):
        """
        Deleting from a linked list.

        The procedure LIST-DELETE Removes an element x from a linked list L.
        It must be given a pointer to x, and it then “splices” x
        out of the list by updating pointers. If we wish to delete an element
        with a given key, we must first call
        LIST-SEARCH to retrieve a pointer to the element.

        Parameters
        ----------
        x : DoublyLinkedList.Element
            The element to delete.

        k : int
            Given key of the element to delete.

        """
        if not x:
            if not k:
                raise ValueError("LIST-DELETE requires either x or key to be given.")
            x = self.list_search(k)
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self._head = x.next
        if x.next is not None:
            x.next.prev = x.prev


class CircularDoublyLinkedList(BaseDoublyLinkedList):
    """
    Circular, doubly linked list with a sentinel.

    # TODO: list_delete reference implementation

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> L = CircularDoublyLinkedList()
    >>> L.list_insert(L.element(1))
    >>> L.list_insert(L.element(4))
    >>> L.list_insert(L.element(16))
    >>> L.list_insert(L.element(9))

    Finds the first element with key 16 in list L

    >>> x = L.list_search(16)
    >>> x
    CircularDoublyLinkedList.Element(key=16, address=0x1fcb744c200)

    Insert an element with key 25 as the new head

    >>> x = L.element(25)
    >>> L.list_insert(x)

    Sentinel
    >>> x.prev
    Element(key=None, address=0x24fcbc7d980)
    >>> x.next
    Element(key=9, address=0x24fcbcb8200)

    To remove an element x from a linked list L

    >>> L.list_delete(1)
    >>> L.list_search(1)
    Element(key=None, address=0x24fcbc7d980)

    It's the sentinel. L does not contain Element with key=1 anymore.

    """

    # This is for the purpose of correct __qualname__ for subclass.
    class Element(BaseDoublyLinkedList.Element):
        pass

    def __init__(self):
        self._sentinel = self.Element(None)
        self._sentinel.next = self._sentinel
        self._sentinel.prev = self._sentinel

    def list_search(self, k):
        """
        Searching a linked list

        Finds the first element with key k in list L
        by a simple linear search, returning a pointer to this element

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : Element
            The element with key k.

        # Notes
        # -----
        # This is Exercises 10.2-4 implementation. For original LIST-SEARCH'(L,k), remove
        #
        # self._sentinel.key = k
        #
        # and replace line
        #
        #     while x.key != k:
        #
        # with
        #
        #     while x is not self._sentinel and x.key != k:

        """
        # self._sentinel.key = k
        x = self._sentinel.next
        while x is not self._sentinel and x.key != k:
            x = x.next
        return x

    def list_insert(self, x):
        """
        Inserting into a linked list.

        Given an element x whose key attribute has already been set,
        LIST INSERT procedure “splices” x onto
        the front of the linked list.

        Parameters
        ----------
        x : Element
            The element to insert.

        """
        x.next = self._sentinel.next
        self._sentinel.next.prev = x
        self._sentinel.next = x
        x.prev = self._sentinel

    # def list_delete(self, x):
    #     """
    #     Deleting from a linked list.
    #
    #     The procedure LIST-DELETE Removes an element x from a linked list L.
    #     It must be given a pointer to x, and it then “splices” x
    #     out of the list by updating pointers. If we wish to delete an element
    #     with a given key, we must first call
    #     LIST-SEARCH to retrieve a pointer to the element.
    #
    #     Parameters
    #     ----------
    #     x : Element
    #         The element to delete.
    #
    #     """
    #     if x.prev is not None:-
    #         x.prev.next = x.next
    #     else:
    #         self._head = x.next
    #     if x.next is not None:
    #         x.next.prev = x.prev

    def list_delete(self, x=None, k=None):
        """
        Deleting from a linked list.

        The procedure LIST-DELETE Removes an element x from a linked list L.
        It must be given a pointer to x, and it then “splices” x
        out of the list by updating pointers. If we wish to delete an element
        with a given key, we must first call
        LIST-SEARCH to retrieve a pointer to the element.

        Parameters
        ----------
        x : DoublyLinkedList.Element
            The element to delete.

        k : int
            Given key of the element to delete.

        """
        if not x:
            if not k:
                raise ValueError("LIST-DELETE requires either x or key to be given.")
            x = self.list_search(k)
        x.prev.next = x.next
        x.next.prev = x.prev


class MultipleArrayDoublyLinkedList:
    """
    Doubly linked list.

    # TODO: list_delete reference implementation

    Unsorted and doubly linked list.

    Attributes
    ----------
    head : Element, default: None
        An attribute L.head points to the first element of the
        list. If L.head=None, the list is empty.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the Stack data structure is:

    >>> L = DoublyLinkedList()

    Use DoublyLinkedList.element(key) to generate a element for doubly linked list

    >>> x = L.element(1)
    >>> L.list_insert(x)
    >>> L.list_insert(L.element(4))
    >>> L.list_insert(L.element(16))
    >>> L.list_insert(L.element(9))
    >>> L.head
    DoublyLinkedList.Element(key=9, address=0x208ea29d300)

    Finds the first element with key 16 in list L

    >>> x = L.list_search(16)
    >>> x
    DoublyLinkedList.Element(key=16, address=0x208ea29c880)

    Insert an element with key 25 as the new head

    >>> x = L.element(25)
    >>> L.list_insert(x)
    >>> L.head
    DoublyLinkedList.Element(key=25, address=0x208ea2b9f40)

    TO remove an element x from a linked list L

    >>> L.list_delete(4)
    >>> L.list_search(4)

    """
    L = ReadOnly()

    def __init__(self, n):
        self.L = 0
        self._next = [None] * n
        self._key = [None] * n
        self._prev = [None] * n
        self._n = n

    def list_search(self, k):
        """
        Searching a linked list

        Finds the first element with key k in list L
        by a simple linear search, returning a pointer to this element

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : Element
            The element with key k.

        """
        x = self.L
        while self._key[x] is not None and self._key[x] != k:
            x = self._next[x]
        return x

    def list_insert(self, x):
        """
        Inserting into a linked list.

        Given an element x whose key attribute has already been set,
        LIST INSERT procedure “splices” x onto
        the front of the linked list.

        Parameters
        ----------
        x : Element
            The element to insert.

        """
        x.next = self._head
        if self._head is not None:
            self._head.prev = x
        self._head = x
        x.prev = None

    # def list_delete(self, x):
    #     """
    #     Deleting from a linked list.
    #
    #     The procedure LIST-DELETE Removes an element x from a linked list L.
    #     It must be given a pointer to x, and it then “splices” x
    #     out of the list by updating pointers. If we wish to delete an element
    #     with a given key, we must first call
    #     LIST-SEARCH to retrieve a pointer to the element.
    #
    #     Parameters
    #     ----------
    #     x : Element
    #         The element to delete.
    #
    #     """
    #     if x.prev is not None:
    #         x.prev.next = x.next
    #     else:
    #         self._head = x.next
    #     if x.next is not None:
    #         x.next.prev = x.prev

    def list_delete(self, k):
        """
        Deleting from a linked list.

        The procedure LIST-DELETE Removes an element x from a linked list L.
        It must be given a pointer to x, and it then “splices” x
        out of the list by updating pointers. If we wish to delete an element
        with a given key, we must first call
        LIST-SEARCH to retrieve a pointer to the element.

        Parameters
        ----------
        k : int
            Given key of the element to delete.

        """
        x = self.list_search(k)
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self._head = x.next
        if x.next is not None:
            x.next.prev = x.prev
