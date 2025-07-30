from data_structures.tree import BinaryTree

__all__ = ["BinarySearchTree"]


class BinarySearchTree(BinaryTree):
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

    # TODO: Tell user how to create a tree with correct insertion order.

    >>> BST = BinarySearchTree()
    >>> x12 = BinarySearchTree.Node(12)
    >>> x18 = BinarySearchTree.Node(18)
    >>> x5 = BinarySearchTree.Node(5)
    >>> x2 = BinarySearchTree.Node(2)
    >>> x9 = BinarySearchTree.Node(9)
    >>> x15 = BinarySearchTree.Node(15)
    >>> x19 = BinarySearchTree.Node(19)
    >>> x17 = BinarySearchTree.Node(17)
    >>> x13 = BinarySearchTree.Node(13)
    >>> BST.tree_insert(x12)
    >>> BST.tree_insert(x18)
    >>> BST.tree_insert(x5)
    >>> BST.tree_insert(x2)
    >>> BST.tree_insert(x9)
    >>> BST.tree_insert(x15)
    >>> BST.tree_insert(x19)
    >>> BST.tree_insert(x17)

    Inserting an item with key 13 into a binary search tree.

    >>> BST.tree_insert(x13)

    >>> x15.left
    BinarySearchTree.Node(key=13, address=0x2b01e24d380)
    >>> x13.p
    BinarySearchTree.Node(key=15, address=0x2b01e24c500)

    Deleting an tree node 15

    >>> x = BinarySearchTree.iterative_tree_search(BST.root, 15)
    >>> BST.tree_delete(x)
    >>> BinarySearchTree.iterative_tree_search(BST.root, 15)

    >>> x = BinarySearchTree.iterative_tree_search(BST.root, 18)
    >>> x.left
    BinarySearchTree.Node(key=17, address=0x2c2bf458bc0)

    Create a binary search tree as Figure 12.1 in CLSR.

    >>> BST_a = BinarySearchTree()
    >>> BST_a.tree_insert(BinarySearchTree.Node(6))
    >>> BST_a.tree_insert(BinarySearchTree.Node(5))
    >>> BST_a.tree_insert(BinarySearchTree.Node(7))
    >>> BST_a.tree_insert(BinarySearchTree.Node(2))
    >>> BST_a.tree_insert(BinarySearchTree.Node(5))
    >>> BST_a.tree_insert(BinarySearchTree.Node(8))

    >>> BST_b = BinarySearchTree()
    >>> BST_b.tree_insert(BinarySearchTree.Node(2))
    >>> BST_b.tree_insert(BinarySearchTree.Node(5))
    >>> BST_b.tree_insert(BinarySearchTree.Node(7))
    >>> BST_b.tree_insert(BinarySearchTree.Node(6))
    >>> BST_b.tree_insert(BinarySearchTree.Node(8))
    >>> BST_b.tree_insert(BinarySearchTree.Node(5))

    Create a generator for inorder tree walk

    >>> inorder_walk = BinarySearchTree.inorder_tree_walk(BST_a.root)
    >>> next(inorder_walk)
    2
    >>> next(inorder_walk)
    5
    >>> next(inorder_walk)
    5
    >>> next(inorder_walk)
    6
    >>> next(inorder_walk)
    7
    >>> next(inorder_walk)
    8

    Instance of BinarySearchTree is a iterable with inorder tree walk as
    iteration order:

    >>> for k in BST_a:
    ...     print(k)
    2
    5
    5
    6
    7
    8

    Similarly for Figure 12.1 (b)

    >>> inorder_walk = BST_b.inorder_tree_walk(BST_b.root)
    >>> for k in inorder_walk:
    ...     print(k)
    2
    5
    5
    6
    7
    8

    preorder and postorder tree walk

    >>> preorder_walk = BinarySearchTree.preorder_tree_walk(BST_a.root)
    >>> for k in preorder_walk:
    ...     print(k)
    6
    5
    2
    5
    7
    8

    >>> postorder_walk = BinarySearchTree.postorder_tree_walk(BST_a.root)
    >>> for k in postorder_walk:
    ...     print(k)
    2
    5
    5
    8
    7
    6

    Create a binary search tree as Figure 12.2 in CLSR.

    >>> BST = BinarySearchTree()
    >>> BST.tree_insert(BinarySearchTree.Node(15))
    >>> BST.tree_insert(BinarySearchTree.Node(6))
    >>> BST.tree_insert(BinarySearchTree.Node(18))
    >>> BST.tree_insert(BinarySearchTree.Node(3))
    >>> BST.tree_insert(BinarySearchTree.Node(7))
    >>> BST.tree_insert(BinarySearchTree.Node(17))
    >>> BST.tree_insert(BinarySearchTree.Node(20))
    >>> BST.tree_insert(BinarySearchTree.Node(2))
    >>> BST.tree_insert(BinarySearchTree.Node(4))
    >>> BST.tree_insert(BinarySearchTree.Node(13))
    >>> BST.tree_insert(BinarySearchTree.Node(9))

    To search for the key 13 in the tree,

    >>> BST.tree_search(BST.root, 13)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    To find the minimum/maximum key in the tree,

    >>> BinarySearchTree.tree_minimum(BST.root)
    BinarySearchTree.Node(key=2, address=0x2c2bf3e8500)
    >>> BinarySearchTree.tree_maximum(BST.root)
    BinarySearchTree.Node(key=20, address=0x2c2bf3e8080)

    Instead of searching min/max from the root, you can search the subtree from any node.
    For example find maximum of subtree starting from node 6,

    >>> x = BinarySearchTree.tree_search(BST.root, 6)
    >>> BinarySearchTree.tree_maximum(x)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    Or to use recursive version,

    >>> BinarySearchTree.recursive_tree_maximum(x)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    The successor of the node with key 13

    >>> x = BinarySearchTree.iterative_tree_search(BST.root, 13)
    >>> succ = BinarySearchTree.tree_successor(x)
    >>> succ
    BinarySearchTree.Node(key=15, address=0x2c2bf3aea40)

    The predecessor of the node with key 13
    >>> pred = BinarySearchTree.tree_predecessor(x)
    >>> pred
    BinarySearchTree.Node(key=9, address=0x2c2bf3e8ac0)

    Children of the node 15

    >>> children = BST.children(BST.root)
    >>> next(children)
    BinaryTree.Node(key=6, address=0x105cc5f80)
    >>> next(children)
    BinaryTree.Node(key=18, address=0x105cc5c40)

    Number of children of node with key 18

    >>> x = BinarySearchTree.tree_search(BST.root, 18)
    >>> BinarySearchTree.n_children(x)
    2

    """

    def __init__(self):
        super().__init__()

    def __getitem__(self, key):
        return self.tree_search(self._root, key)

    def __setitem__(self, key, value):
        raise NotImplementedError("__setitem__ is not implemented for BinarySearchTree.")

    def __delitem__(self, key):
        z = self.tree_search(self._root, key)
        if z:
            self.tree_delete(z)

    # root = ReadOnly()
    #
    # class Node:
    #     """
    #     The node of a binary search tree T
    #
    #     An object in addition to a key and satellite data,
    #     each node contains attributes left, right, and p that point
    #      to the nodes corresponding to its left child,
    #     its right child, and its parent, respectively.
    #
    #     Attributes
    #     ----------
    #     key : object
    #         The key of this node.
    #
    #     left : object, default: None
    #         The left child of this node.
    #
    #     right : object, default: None
    #         The right child of this node.
    #
    #     p : object, default: None
    #         The parent of this node.
    #
    #     Examples
    #     --------
    #     Create an node with key 6:
    #
    #     >>> x = BinarySearchTree.Node(6)
    #     >>> x
    #     BinarySearchTree.Node(key=6, left=None, right=None, p=None), address=0x1f0f7d8d540)
    #
    #     """
    #     __slots__ = ["key", "left", "right", "p"]
    #
    #     def __init__(self, key, left=None, right=None, p=None):
    #         self.key = key
    #         self.left = left
    #         self.right = right
    #         self.p = p
    #
    #     def __repr__(self):
    #         return (f"{self.__class__.__qualname__}(key={self.key}, "
    #                 # f"left={self.left}, "
    #                 # f"right={self.right}, "
    #                 # f"p={self.p}), "
    #                 f"address={hex(id(self))})")
    #
    #     def __eq__(self, other):
    #         return other is self
    #
    #     def __ne__(self, other):
    #         """Return True if other does not represent the same Node"""
    #         return not (self == other)


    # def node(self, k):
    #     """
    #     Generate a node with key k.
    #
    #     Parameters
    #     ----------
    #     k : int
    #         The node with key k.
    #
    #     Returns
    #     -------
    #     element : BinarySearchTree.Node
    #         The node with key k.
    #     """
    #     return self.__class__.Node(k)

    def __iter__(self):
        yield from (k for k in self.inorder_tree_walk(self._root))

    # @staticmethod
    # def inorder_tree_walk(x):
    #     """Inorder tree walk recursive procedure
    #
    #     Parameters
    #     ----------
    #     x : BinarySearchTree.Node
    #         Given node x.
    #
    #     Yields
    #     ------
    #     inorder_walk : int
    #          The key of the root of a subtree between yielding the values in its left subtree
    #         and yielding those in its right subtree.
    #
    #     """
    #     if x:
    #         yield from BinarySearchTree.inorder_tree_walk(x.left)
    #         yield x.key
    #         yield from BinarySearchTree.inorder_tree_walk(x.right)
    #
    # @staticmethod
    # def iterative_inorder_tree_walk(x):
    #     """Inorder tree walk iterative procedure
    #
    #     # TODO: order is still wrong
    #     It yields the key of the root of a subtree
    #     between yielding the values in its left subtree
    #     and yielding those in its right subtree.
    #
    #     Parameters
    #     ----------
    #     x : BinarySearchTree.Node
    #         Given node x.
    #
    #     Yields
    #     ------
    #     inorder_walk : int
    #          The key of the root of a subtree between yielding the values in its left subtree
    #         and yielding those in its right subtree.
    #
    #     """
    #     s = Stack(20)
    #     s.push(x)
    #     while not s.stack_empty():
    #         z = s.pop()
    #         if z:
    #             yield z.key
    #             s.push(z.right)
    #             s.push(z.left)
    #
    # @staticmethod
    # def preorder_tree_walk(x):
    #     """Preorder tree walk recursive procedure
    #
    #     Parameters
    #     ----------
    #     x : BinarySearchTree.Node
    #         Given node x.
    #
    #     Yields
    #     ------
    #     preorder_walk : int
    #         Yields the root before the values in either subtree.
    #
    #     """
    #     if x:
    #         yield x.key
    #         yield from BinarySearchTree.preorder_tree_walk(x.left)
    #         yield from BinarySearchTree.preorder_tree_walk(x.right)
    #
    # @staticmethod
    # def postorder_tree_walk(x):
    #     """Postorder tree walk recursive procedure
    #
    #     Parameters
    #     ----------
    #     x : BinarySearchTree.Node
    #         Given node x.
    #
    #     Yields
    #     ------
    #     postorder_walk : int
    #         Yields the root after the values in its subtrees.
    #
    #     """
    #     if x:
    #         yield from BinarySearchTree.postorder_tree_walk(x.left)
    #         yield from BinarySearchTree.postorder_tree_walk(x.right)
    #         yield x.key

    @staticmethod
    def tree_search(x, k):
        """TREE SEARCH recursive procedure.

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

        Returns
        -------
        res : BinarySearchTree.Node
            Returns a pointer to a node with key k if one exists;
            otherwise, it returns None.

        """
        if x is None or k == x.key:
            return x
        if k < x.key:
            return BinarySearchTree.tree_search(x.left, k)
        else:
            return BinarySearchTree.tree_search(x.right, k)

    @staticmethod
    def iterative_tree_search(x, k):
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

        Returns
        -------
        res : BinarySearchTree.Node
            Returns a pointer to a node with key k if one exists;
            otherwise, it returns None.

        """
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @staticmethod
    def tree_minimum(x):
        """
        TREE MINIMUM iterative procedure

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        min : BinarySearchTree.Node
            Returns a pointer to the minimum element
            in the subtree rooted at a given node x.

        """
        while x.left is not None:
            x = x.left
        return x

    @staticmethod
    def tree_maximum(x):
        """
        TREE MAXIMUM iterative procedure

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        max : BinarySearchTree.Node
            Returns a pointer to the maximum element in
            the subtree rooted at a given node x.

        """
        while x.right is not None:
            x = x.right
        return x

    @staticmethod
    def recursive_tree_minimum(x):
        """
        TREE MINIMUM recursive procedure

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        min : BinarySearchTree.Node
            Returns a pointer to the minimum element
            in the subtree rooted at a given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x.left is not None:
            return BinarySearchTree.recursive_tree_minimum(x.left)
        else:
            return x

    @staticmethod
    def recursive_tree_maximum(x):
        """
        TREE MAXIMUM recursive procedure

        Returns a pointer to the maximum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        max : BinarySearchTree.Node
            Returns a pointer to the maximum element
            in the subtree rooted at a given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x.right is not None:
            return BinarySearchTree.recursive_tree_maximum(x.right)
        else:
            return x

    @staticmethod
    def tree_successor(x):
        """TREE SUCCESSOR procedure

        Find its successor in the sorted order
        determined by an inorder tree walk. If all keys are distinct,
        the successor of a node x is the node with the
        smallest key greater than x.key.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        succ : BinarySearchTree.Node
            Returns a pointer to the successor element
            in the subtree rooted at a given node x.

        """
        if x.right:
            return BinarySearchTree.tree_minimum(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    @staticmethod
    def tree_predecessor(x):
        """TREE PREDECESSOR procedure

        Find its predecessor in the sorted order
        determined by an inorder tree walk. If all keys are distinct,
        the predecessor of a node x is the node with the
        largest key less than x.key.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        Returns
        -------
        pred : BinarySearchTree.Node
            Returns a pointer to the predecessor element
            in the subtree rooted at a given node x.

        """
        if x.left:
            return BinarySearchTree.tree_maximum(x.left)
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
        self._n += 1

    def transplant(self, u, v):
        """
        Subroutine TRANSPLANT
        
        Which replaces one subtree as a child of its
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

        # TODO: implement self._n size change.

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
