
from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping

from ._linked_list import DoublyLinkedList
# from ..utils import (
#     ReadOnly,
# )
from exceptions import HashTableOverflowError
from utils import ReadOnly

__all__ = ["DirectAddressTable",
           "BitVector",
           "HashTable",
           "OpenAddressingHashTable"]


class DirectAddressTable:
    """
    Direct Address Table.

    Parameters
    ----------
    m : int
        A direct address table of at most m elements with an array T[0..m-1].

    Attributes
    ----------
    T : list
        A direct address table of at most m elements with an array T[0..m-1].

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the DirectAddressTable data structure is:

    >>> T = DirectAddressTable(10)
    >>> T.m
    10

    Use DirectAddressTalbe.element(key, v) to generate an element for direct address table
    >>> e = T.element(2, 3)
    >>> e
    DirectAddressTable.Element(key=2, satellite_data=3, address=0x1a21b3a21d0)

    >>> T.direct_address_insert(e)
    >>> T.direct_address_insert(T.element(3, 7))
    >>> T.direct_address_insert(T.element(5, 2))
    >>> T.direct_address_insert(T.element(8, -1))

    Search for the element with key 3 in DirectAddressTable T

    >>> e = T.direct_address_search(3)
    >>> e
    DirectAddressTable.Element(key=3, satellite_data=7, address=0x1a21b3a2410)

    Delete an element in DirectAddressTable T

    >>> T.direct_address_delete(e)
    >>> T.T
    [None,
     None,
     DirectAddressTable.Element(key=2, satellite_data=3, address=0x1a21b3a02e0),
     None,
     None,
     DirectAddressTable.Element(key=5, satellite_data=2, address=0x1a21b3a0b20),
     None,
     None,
     DirectAddressTable.Element(key=8, satellite_data=-1, address=0x1a21b3a2da0),
     None]

    """

    T = ReadOnly()
    m = ReadOnly()

    class Element:
        """
        The element of a direct address table.

        Abn object with an attribute key and
        satellite data.

        Attributes
        ----------
        key : object, default: None
            The key of this element.

        satellite_data : object, default: None
            The satellite data of this element.

        Examples
        --------
        Create an element with key 25:

        >>> x = L.element(25)
        >>> x
        SinglyLinkedList.Element(key=25, address=0x2490300da50)

        """

        __slots__ = ["key", "satellite_data"]

        def __init__(self, key, v):
            self.key = key
            self.satellite_data = v

        def __repr__(self):
            return (f"{self.__class__.__qualname__}"
                    f"(key={self.key}, "
                    f"satellite_data={self.satellite_data}, "
                    f"address={hex(id(self))})")


    def __init__(self, m):
        self._T = [None] * m
        self._m = m

    def element(self, k, v):
        """
        Generate a element with key k and satellite data v.

        Parameters
        ----------
        k : int
            The element with key k.

        v : object
            The satellite_data v.

        Returns
        -------
        element : DirectAddressTable.Element
            The element with key k and satellite data v.

        """
        return self.__class__.Element(k, v)

    def direct_address_search(self, k):
        """
        Searching a Direct Address Table.

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : DirectAddressTable.Element
            The element with key k.

        """
        return self._T[k]

    def direct_address_insert(self, x):
        """
        The INSERT operation on a DirectAddressTable.

        Parameters
        ----------
        x : DirectAddressTable.Element
            The element to be inserted.

        """
        self._T[x.key] = x

    def direct_address_delete(self, x):
        """
        The DELETE operation on a DirectAddressTable.

        Parameters
        ----------
        x : DirectAddressTable.Element
            The element to be deleted.

        """
        self._T[x.key] = None

    def direct_address_maximum(self):
        """
        Finds the maximum element of T

        Returns
        -------
        max : DirectAddressTable.Element
            The maximum element of T

        Notes
        -----
        See CLRS Exercises 11.1-1

        Examples
        --------
        >>> T = DirectAddressTable(10)
        >>> T.direct_address_insert(T.element(2, 3))
        >>> T.direct_address_insert(T.element(3, 7))
        >>> T.direct_address_insert(T.element(5, 2))
        >>> T.direct_address_insert(T.element(8, -1))
        >>> T.direct_address_maximum()
        DirectAddressTable.Element(key=8, satellite_data=-1, address=0x21133fa1ab0)

        """
        for i in range(self._m - 1, 0, -1):
            if self._T[i]:
                return self._T[i]
        return None


class BitVector:
    """
    Bit Vector.

    Parameters
    ----------
    m : int
        A bit vector of at most m elements with an array B[0..m-1].

    Attributes
    ----------
    B : list
        A bit vector of at most m elements with an array T[0..m-1].

    Notes
    -----
    See CLRS Exercises 11.1-2.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the BitVector data structure is:

    >>> B = BitVector(10)
    >>> B.m
    10

    >>> B.bit_vector_insert(2)
    >>> B.bit_vector_insert(4)
    >>> B.bit_vector_insert(6)
    >>> B.B
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0]

    >>> e = B.bit_vector_search(3)
    >>> e
    None

    >>> e = B.bit_vector_search(4)
    >>> e
    4

    Delete an element in BitVector B

    >>> B.bit_vector_delete(4)
    >>> B.B
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

    """

    B = ReadOnly()
    m = ReadOnly()

    def __init__(self, m):
        self._B = [0] * m
        self._m = m

    def bit_vector_search(self, k):
        """
        Searching a Bit Vector.

        Parameters
        ----------
        k : int
            Key k.

        Returns
        -------
        element :
            Return k if B[k] == 1, else None

        """
        return k if self._B[k] == 1 else None

    def bit_vector_insert(self, k):
        """
        The INSERT operation on a BitVector.

        Parameters
        ----------
        k : int
            Key k.

        """
        self._B[k] = 1

    def bit_vector_delete(self, k):
        """
        The DELETE operation on a BitVector.

        Parameters
        ----------
        k : int
            Key k.

        """
        self._B[k] = 0


class BaseHashTable(MutableMapping, metaclass=ABCMeta):
    """Base class for hash tables."""

    T = ReadOnly()
    m = ReadOnly()
    h = ReadOnly()
    n = ReadOnly()

    def __init__(self, m, h):
        self._T = [None] * m
        self._m = m
        self._h = h
        self._n = 0

    def __len__(self):
        return self._n


class HashTable(BaseHashTable):
    """
    HashTable with collision resolution by chaining.

    Parameters
    ----------
    m : int
        A hash table of at most m elements with an array T[0..m-1].

    h : function
        Hash function h to compute the slot from the key k.
        Here, h maps the universe U of keys into the slots of a hash table
        T[0..m-1]:

        h : U -> {0, 1,..., m-1}.

    Attributes
    ----------
    T : list
        A hash table of at most m elements with an array T[0..m-1].

    n : int
        The number of distinct items that are currently stored in the hash table.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the HashTable data structure is:

    Let the hash function be h(k) = k mod 9
    >>> from data_structures import DivisionMethod
    >>> m = 9
    >>> h = DivisionMethod(m).h()
    >>> T = HashTable(m, h)
    >>> T.m
    9

    As in CLRS Exercises 11.2-2., we insert the keys 5, 28, 19, 15, 20, 33, 12, 17, 10
    into a hash table with collisions resolved by chaining.

    >>> L = DoublyLinkedList()
    >>> T.chained_hash_insert(L.element(5))
    >>> T.chained_hash_insert(L.element(28))
    >>> T.chained_hash_insert(L.element(19))
    >>> T.chained_hash_insert(L.element(15))
    >>> T.chained_hash_insert(L.element(20))
    >>> T.chained_hash_insert(L.element(33))
    >>> T.chained_hash_insert(L.element(12))
    >>> T.chained_hash_insert(L.element(17))
    >>> T.chained_hash_insert(L.element(10))

    Search on hash table T for key=28

    >>> e = T.chained_hash_search(28)
    >>> e
    DoublyLinkedList.Element(key=28, address=0x1f901934340)

    Or indexing,
    >>> T[28]
    DoublyLinkedList.Element(key=28, address=0x1f901934340)

    Delete this element in T, either

    >>> T.chained_hash_delete(e)

    Or index delete,
    >>> del T[28]

    >>> T.chained_hash_search(28)

    >>> T.T
    [None,
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=10, address=0x16e832e4c80)),
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=20, address=0x16e832e4380)),
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=12, address=0x16e832e4d00)),
     None,
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=5, address=0x16e832be940)),
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=33, address=0x16e832e4480)),
     None,
     DoublyLinkedList.Element(head=DoublyLinkedList.Element(key=17, address=0x16e832e5340))]

    """

    def __init__(self, m, h):
        super().__init__(m, h)

    def __getitem__(self, key):
        return self.chained_hash_search(key)

    # def __setitem__(self, key, value):
    #     x = self.chained_hash_search(key)
    #     if not x:
    #         L = DoublyLinkedList()
    #         self.chained_hash_insert(L.element(key))
    #     else:
    #         x.key = value
    def __setitem__(self, key, value):
        raise NotImplementedError("__setitem__ is not implemented for HashTable type.")

    def __delitem__(self, key):
        x = self.chained_hash_search(key)
        if not x:
            raise KeyError(f"Key Error: {key} not found.")
        else:
            self.chained_hash_delete(x)

    def __iter__(self):
        raise NotImplementedError("__iter__ is not implemented for HashTable type.")

    def chained_hash_search(self, k):
        """
        CHAINED-HASH-SEARCH in HashTable.

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : DoublyLinkedList.Element
            The element with key k.

        """
        if not self._T[self._h(k)]:
            return None
        return self._T[self._h(k)].list_search(k)

    def _chained_hash_insert(self, x):
        if not self._T[self._h(x.key)]:
            self._T[self._h(x.key)] = DoublyLinkedList()
        self._T[self._h(x.key)].list_insert(x)
        self._n += 1

    def chained_hash_insert(self, x, presence_check=False):
        """
        CHAINED-HASH-INSERT in HashTable.

        Parameters
        ----------
        x : DoublyLinkedList.Element
            The element to be inserted.

        presence_check : bool, default False
            It assumes that the element x being inserted is not already present in
            the table; Check this assumption (at additional cost) by searching
            for an element whose key is x.key before we insert.

        """
        if presence_check:
            if not self.chained_hash_search(x.key):
                self._chained_hash_insert(x)
            else:
                raise ValueError("The element x already present in the table.")
        else:
            self._chained_hash_insert(x)

    def chained_hash_delete(self, x):
        """
        CHAINED-HASH-DELETE in HashTable.

        Parameters
        ----------
        x : DoublyLinkedList.Element
            The element to be deleted.

        """
        if self._T[self._h(x.key)]:
            self._T[self._h(x.key)].list_delete(x)
            self._n -= 1


class OpenAddressingHashTable(BaseHashTable):
    """
    HashTable with collision resolution by open addressing.

    # TODO: delete has something wrong

    Parameters
    ----------
    m : int
        A hash table of at most m elements with an array T[0..m-1].

    h : function
        Hash function h to compute the slot from the key k.
        Here, h maps the universe U of keys into the slots of a hash table
        T[0..m-1]:

        h : U -> {0, 1,..., m-1}.

    Attributes
    ----------
    T : list
        A hash table of at most m elements with an array T[0..m-1].

    n : int
        The number of distinct items that are currently stored in the hash table.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the OpenAddressingHashTable data structure is:

    As in CLRS Exercises 11.4-1, consider inserting the keys 10, 22, 31, 4, 15, 28, 17, 88, 59 into a hash table of
    length m=11 using open addressing with the auxiliary hash function h'(k) = k

    >>> from data_structures import LinearProbing, QuadraticProbing, DoubleHashing
    >>> m = 11
    >>> h_prime = lambda k: k
    >>> keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]

    linear probing
    >>> h = LinearProbing(m, h_prime).h()
    >>> T = OpenAddressingHashTable(m, h)
    >>> T.m
    9

    >>> for k in keys:
    ...     T.hash_insert(k)
    >>> T.T
    [22, 88, None, None, 4, 15, 28, 17, 59, 31, 10]

    quadratic probing
    >>> c_1 = 1
    >>> c_2 = 3
    >>> h = QuadraticProbing(m, c_1, c_2, h_prime).h()
    >>> T = OpenAddressingHashTable(m, h)

    >>> for k in keys:
    ...     T.hash_insert(k)
    >>> T.T
    [22, None, 88, 17, 4, None, 28, 59, 15, 31, 10]

    double hashing
    >>> h_1 = h_prime
    >>> h_2 = lambda k: 1 + k % (m - 1)
    >>> h = DoubleHashing(m, h_1, h_2).h()
    >>> T = OpenAddressingHashTable(m, h)

    >>> for k in keys:
    ...     T.hash_insert(k)
    >>> T.T
    [22, None, 59, 17, 4, 15, 28, 88, None, 31, 10]

    Search on hash table T for key=28

    >>> j = T.hash_search(28)
    >>> j
    6

    Or indexing,
    >>> T[28]
    6

    Delete this element in T, either

    >>> T.hash_delete(28)
    6

    Or index delete,
    >>> del T[28]
    6

    # TODO: here delete wrong
    >>> T.chained_hash_search(28)

    >>> T.T
    [22, None, 59, 17, 4, 15, <object at 0x1e51aa45790>, 88, None, 31, 10]

    """

    _Deleted = object()  # special value DELETED for Deletion from an open-address hash table.

    def __init__(self, m, h):
        super().__init__(m, h)

    def __getitem__(self, key):
        return self.hash_search(key)

    def __setitem__(self, key, value):
        x = self.hash_search(key)
        if not x:
            self._T[key] = value
            self._n += 1
        else:
            self._T[key] = value

    def __delitem__(self, key):
        x = self.hash_search(key)
        if not x:
            raise KeyError(f"Key Error: {key} not found.")
        else:
            self.hash_delete(key)

    def hash_insert(self, k):
        """
        HASH-INSERT in OpenAddressingHashTable.

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        j : int
            The slot number where it stores key k.

        Raises
        ------
        HashTableOverflowError
            If the hash table is already full.

        """
        i = 0
        while i != self._m:
            j = self._h(k, i)
            if self._T[j] is None or self._T[j] is OpenAddressingHashTable._Deleted:
                self._T[j] = k
                self._n += 1
                return j
            else:
                i += 1
        raise HashTableOverflowError("Hash table overflow.")

    def hash_search(self, k):
        """
        HASH-SEARCH in OpenAddressingHashTable.

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : DoublyLinkedList.Element
            The element with key k.

        """
        i = 0
        while self._T[i] is not None or i != self._m:
            j = self._h(k, i)
            if self._T[j] == k:
                return j
            i += 1
        return None

    def hash_delete(self, k):
        """
        HASH-DELETE in OpenAddressingHashTable.

        Parameters
        ----------
        k : int
            The element with key k.

        Returns
        -------
        element : DoublyLinkedList.Element
            The element with key k.

        Raises
        ------
        KeyError
            If the key not found in the hash table.

        """
        i = 0
        while self._T[i] is not None or i != self._m:
            j = self._h(k, i)
            if self._T[j] == k:
                self._T[j] = OpenAddressingHashTable._Deleted
                self._n -= 1
                return j
            else:
                i += 1
        raise KeyError(f"Key Error: {k} not found.")

    def __iter__(self):
        """
        TODO: implement
        Returns
        -------

        """
        raise NotImplementedError("Iteration not implemented.")


