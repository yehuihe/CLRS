from data_structures import Stack
from utils import ReadOnly

__all__ = ["BinarySearchTree"]


class BinarySearchTree:
    """
    Binary Search Tree.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the BinarySearchTree data structure is:

    Create a binary search tree as Figure 12.3 in CLSR.

    >>> BST = BinarySearchTree()
    >>> BST.tree_insert(BinarySearchTree.Node(2))
    >>> BST.tree_insert(BinarySearchTree.Node(5))
    >>> BST.tree_insert(BinarySearchTree.Node(9))
    >>> BST.tree_insert(BinarySearchTree.Node(12))
    >>> BST.tree_insert(BinarySearchTree.Node(18))
    >>> BST.tree_insert(BinarySearchTree.Node(15))
    >>> BST.tree_insert(BinarySearchTree.Node(19))
    >>> BST.tree_insert(BinarySearchTree.Node(17))

    Now inserting an item with key 13 into a binary search tree.

    >>> BST.tree_insert(BinarySearchTree.Node(13))



    """
    root = ReadOnly()

    class Node:
        """
        The node of a binary search tree T

        An object in addition to a key and satellite data,
        each node contains attributes left, right, and p that point
         to the nodes corresponding to its left child,
        its right child, and its parent, respectively.

        Attributes
        ----------
        key : object
            The key of this node.

        left : object, default: None
            The left child of this node.

        right : object, default: None
            The right child of this node.

        p : object, default: None
            The parent of this node.

        Examples
        --------
        Create an node with key 6:

        >>> x = BinarySearchTree.Node(6)
        >>> x
        BinarySearchTree.Node(key=6, left=None, right=None, p=None), address=0x1f0f7d8d540)

        """
        __slots__ = ["key", "left", "right", "p"]

        def __init__(self, key, left=None, right=None, p=None):
            self.key = key
            self.left = left
            self.right = right
            self.p = p

        def __repr__(self):
            return (f"{self.__class__.__qualname__}(key={self.key}, "
                    f"left={self.left}, "
                    f"right={self.right}, "
                    f"p={self.p}), "
                    f"address={hex(id(self))})")

        def __eq__(self, other):
            return other is self

        def __ne__(self, other):
            """Return True if other does not represent the same Node"""
            return not (self == other)

    def __init__(self):
        self._root = None

    def node(self, k):
        """
        Generate a node with key k.

        Parameters
        ----------
        k : int
            The node with key k.

        Returns
        -------
        element : BinarySearchTree.Node
            The node with key k.
        """
        return self.__class__.Node(k)

    def tree_search(self, x, k):
        """TREE SEARCH recursive procedure

        To search for a node with a given key in a binary search tree.

        Given a pointer to the root of the tree and a key k, TREE-SEARCH
        returns a pointer to a node with key k
        if one exists; otherwise, it returns None.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        k : int
            The key k to search.

        """
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        """TREE SEARCH iterative procedure

        To search for a node with a given key in a binary search tree.

        Given a pointer to the root of the tree and a key k, TREE-SEARCH
        returns a pointer to a node with key k
        if one exists; otherwise, it returns None.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        k : int
            The key k to search.

        """
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x):
        """
        TREE MINIMUM iterative procedure

        Returns a pointer to the minimum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        while x.left is not None:
            x = x.left
        return x

    def tree_maximum(self, x):
        """
        TREE MAXIMUM iterative procedure

        Returns a pointer to the maximum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        while x.right is not None:
            x = x.right
        return x

    def recursive_tree_minimum(self, x):
        """
        TREE MINIMUM recursive procedure

        Returns a pointer to the minimum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x.left is not None:
            return self.recursive_tree_minimum(x.left)
        else:
            return x

    def recursive_tree_maximum(self, x):
        """
        TREE MAXIMUM recursive procedure

        Returns a pointer to the maximum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x.right is not None:
            return self.recursive_tree_maximum(x.right)
        else:
            return x

    def inorder_tree_walk(self, x):
        """Inorder tree walk recursive procedure

        It yields the key of the root of a subtree
        between yielding the values in its left subtree
        and yielding those in its right subtree.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        if x:
            self.inorder_tree_walk(x.left)
            yield x.key
            self.inorder_tree_walk(x.right)

    def iterative_inorder_tree_walk(self, x):
        """Inorder tree walk iterative procedure

        It yields the key of the root of a subtree
        between yielding the values in its left subtree
        and yielding those in its right subtree.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        s = Stack(20)
        s.push(x)
        while not s.stack_empty():
            z = s.pop()
            if z:
                yield z.key
                s.push(z.left)
                s.push(z.right)

    def preorder_tree_walk(self, x):
        """Preorder tree walk recursive procedure

        It yields the root before the values in either subtree.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        if x:
            yield x.key
            self.preorder_tree_walk(x.left)
            self.preorder_tree_walk(x.right)

    def postorder_tree_walk(self, x):
        """Postorder tree walk recursive procedure

        It yields the root after the values in its subtrees.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        if x:
            self.postorder_tree_walk(x.left)
            self.postorder_tree_walk(x.right)
            yield x.key

    def tree_successor(self, x):
        """TREE SUCCESSOR procedure

        Find its successor in the sorted order
        determined by an inorder tree walk. If all keys are distinct,
        the successor of a node x is the node with the
        smallest key greater than x.key.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        if x.right:
            return self.tree_minimum(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x):
        """TREE PREDECESSOR procedure

        Find its predecessor in the sorted order
        determined by an inorder tree walk. If all keys are distinct,
        the predecessor of a node x is the node with the
        largest key less than x.key.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        if x.left:
            return self.tree_maximum(x.left)
        y = x.p
        while y is not None and x == y.left:
            x = y
            y = y.p
        return y

    def tree_insert(self, z):
        """
        TREE INSERT iterative procedure.

        To insert a new value v into a binary search tree T.

        It modifies T and some of the attributes of z in such a way that
        it inserts z into an appropriate position in the tree

        Parameters
        ----------
        z : BinarySearchTree.Node
            The node z to insert.

        """
        y = None
        x = self._root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self._root = z  # tree T was empty
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        """
        Subroutine TRANSPLANT
        
        hich replaces one subtree as a child of its
        parent with another subtree.

        Parameters
        ----------
        u : BinarySearchTree.Node
            The subtree rooted at node u.

        v : BinarySearchTree.Node
            The subtree rooted at node v.

        """
        if u.p is None:
            self._root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def tree_delete(self, z):
        """
        Deleting a node z from a binary search tree T.

        Parameters
        ----------
        z : BinarySearchTree.Node
            The node z to delete.

        """
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def tree_sort(self, A):
        pass

