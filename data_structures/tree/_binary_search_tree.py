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

    >>> from data_structures.tree import BinarySearchTree
bst = BinarySearchTree()
x12 = BinarySearchTree.Node(12)
x18 = BinarySearchTree.Node(18)
x5 = BinarySearchTree.Node(5)
x2 = BinarySearchTree.Node(2)
x9 = BinarySearchTree.Node(9)
x15 = BinarySearchTree.Node(15)
x19 = BinarySearchTree.Node(19)
x17 = BinarySearchTree.Node(17)
x13 = BinarySearchTree.Node(13)
bst.tree_insert(x12)
bst.tree_insert(x18)
bst.tree_insert(x5)
bst.tree_insert(x2)
bst.tree_insert(x9)
bst.tree_insert(x15)
bst.tree_insert(x19)
bst.tree_insert(x17)

    Inserting an item with key 13 into a binary search tree.

    >>> bst.tree_insert(x13)

    >>> x15.left
    BinarySearchTree.Node(key=13, address=0x2b01e24d380)
    >>> x13.p
    BinarySearchTree.Node(key=15, address=0x2b01e24c500)

    Deleting an tree node 15

    >>> x = bst.iterative_tree_search(15)
    >>> bst.tree_delete(x)
    >>> bst.iterative_tree_search(15)
    <data_structures.tree._binary_search_tree.BinarySearchTree.NIL at 0x103260150>

    >>> x = bst.iterative_tree_search(18)
    >>> x.left
    BinarySearchTree.Node(key=17, address=0x2c2bf458bc0)

    Create a binary search tree as Figure 12.1 in CLSR.

    >>> bst_a = BinarySearchTree()
    >>> bst_a.tree_insert(BinarySearchTree.Node(6))
    >>> bst_a.tree_insert(BinarySearchTree.Node(5))
    >>> bst_a.tree_insert(BinarySearchTree.Node(7))
    >>> bst_a.tree_insert(BinarySearchTree.Node(2))
    >>> bst_a.tree_insert(BinarySearchTree.Node(5))
    >>> bst_a.tree_insert(BinarySearchTree.Node(8))

    >>> bst_b = BinarySearchTree()
    >>> bst_b.tree_insert(BinarySearchTree.Node(2))
    >>> bst_b.tree_insert(BinarySearchTree.Node(5))
    >>> bst_b.tree_insert(BinarySearchTree.Node(7))
    >>> bst_b.tree_insert(BinarySearchTree.Node(6))
    >>> bst_b.tree_insert(BinarySearchTree.Node(8))
    >>> bst_b.tree_insert(BinarySearchTree.Node(5))

    Create a generator for inorder tree walk

    >>> inorder_walk = bst_a.inorder_tree_walk()
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

    >>> for k in bst_a:
    ...     print(k)
    2
    5
    5
    6
    7
    8

    Providing a subtree inorder traversal:

    >>> x = bst_a.tree_search(7)
    >>> for i in bst_a.inorder_tree_walk(x):
    ...     print(i)
    7
    8

    Similarly for Figure 12.1 (b)

    >>> inorder_walk = bst_b.inorder_tree_walk()
    >>> for k in inorder_walk:
    ...     print(k)
    2
    5
    5
    6
    7
    8

    preorder and postorder tree walk

    >>> preorder_walk = bst_a.preorder_tree_walk()
    >>> for k in preorder_walk:
    ...     print(k)
    6
    5
    2
    5
    7
    8

    >>> postorder_walk = bst_a.postorder_tree_walk()
    >>> for k in postorder_walk:
    ...     print(k)
    2
    5
    5
    8
    7
    6

    Create a binary search tree as Figure 12.2 in CLSR.

    >>> bst = BinarySearchTree()
    >>> bst.tree_insert(BinarySearchTree.Node(15))
    >>> bst.tree_insert(BinarySearchTree.Node(6))
    >>> bst.tree_insert(BinarySearchTree.Node(18))
    >>> bst.tree_insert(BinarySearchTree.Node(3))
    >>> bst.tree_insert(BinarySearchTree.Node(7))
    >>> bst.tree_insert(BinarySearchTree.Node(17))
    >>> bst.tree_insert(BinarySearchTree.Node(20))
    >>> bst.tree_insert(BinarySearchTree.Node(2))
    >>> bst.tree_insert(BinarySearchTree.Node(4))
    >>> bst.tree_insert(BinarySearchTree.Node(13))
    >>> bst.tree_insert(BinarySearchTree.Node(9))

    To search for the key 13 in the tree,

    >>> bst.tree_search(13)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    To find the minimum/maximum key in the tree,

    >>> bst.tree_minimum()
    BinarySearchTree.Node(key=2, address=0x2c2bf3e8500)
    >>> bst.tree_maximum()
    BinarySearchTree.Node(key=20, address=0x2c2bf3e8080)

    Instead of searching min/max from the root, you can search the subtree from any node.
    For example find maximum of subtree starting from node 6,

    >>> x = bst.tree_search(6)
    >>> bst.tree_maximum(x)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    Or to use recursive version,

    >>> bst.recursive_tree_maximum(x)
    BinarySearchTree.Node(key=13, address=0x2c2bf3e8b40)

    The successor of the node with key 13

    >>> x = bst.iterative_tree_search(13)
    >>> succ = bst.tree_successor(x)
    >>> succ
    BinarySearchTree.Node(key=15, address=0x2c2bf3aea40)

    The predecessor of the node with key 13
    >>> pred = bst.tree_predecessor(x)
    >>> pred
    BinarySearchTree.Node(key=9, address=0x2c2bf3e8ac0)

    Children of the node 15

    >>> children = bst.children(bst.root)
    >>> next(children)
    BinaryTree.Node(key=6, address=0x105cc5f80)
    >>> next(children)
    BinaryTree.Node(key=18, address=0x105cc5c40)

    Number of children of node with key 18

    >>> x = bst.tree_search(18)
    >>> bst.n_children(x)
    2

    """

    class Node(BinaryTree.Node):
        pass

    class NIL:
        """Dummy for None-nil compatibility."""
        def isnil(self):
            return True

    _NIL = NIL()

    def __init__(self):
        super().__init__()
        self._root = self._NIL

    def __getitem__(self, key):
        return self.tree_search(self._root, key)

    def __setitem__(self, key, value):
        raise NotImplementedError("__setitem__ is not implemented for BinarySearchTree.")

    def __delitem__(self, key):
        z = self.tree_search(self._root, key)
        if z:
            self.tree_delete(z)

    def __iter__(self):
        yield from (k for k in self.inorder_tree_walk())

    def tree_search(self, k, x=None):
        """TREE SEARCH recursive procedure.

        To search for a node with a given key in a binary search tree.

        Given a pointer to the root of the tree and a key k, TREE-SEARCH
        returns a pointer to a node with key k
        if one exists; otherwise, it returns None.

        Parameters
        ----------
        k : int
            The key k to search.

        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        res : BinarySearchTree.Node
            Returns a pointer to a node with key k if one exists;
            otherwise, it returns None.

        """
        if x is None:
            x = self._root

        if x.isnil() or k == x.key:
            return x
        if k < x.key:
            return self.tree_search(k, x.left)
        else:
            return self.tree_search(k, x.right)

    def iterative_tree_search(self, k, x=None):
        """TREE SEARCH iterative procedure

        To search for a node with a given key in a binary search tree.

        Given a pointer to the root of the tree and a key k, TREE-SEARCH
        returns a pointer to a node with key k
        if one exists; otherwise, it returns None.

        Parameters
        ----------
        k : int
            The key k to search.

        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        res : BinarySearchTree.Node
            Returns a pointer to a node with key k if one exists;
            otherwise, it returns None.

        """
        if x is None:
            x = self._root

        while not x.isnil() and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x=None):
        """
        TREE MINIMUM iterative procedure

        Parameters
        ----------
        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        min : BinarySearchTree.Node
            Returns a pointer to the minimum element
            in the subtree rooted at a given node x.

        """
        if x is None:
            x = self._root

        while not x.left.isnil():
            x = x.left
        return x

    def tree_maximum(self, x=None):
        """
        TREE MAXIMUM iterative procedure

        Parameters
        ----------
        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        max : BinarySearchTree.Node
            Returns a pointer to the maximum element in
            the subtree rooted at a given node x.

        """
        if x is None:
            x = self._root

        while not x.right.isnil():
            x = x.right
        return x

    def recursive_tree_minimum(self, x=None):
        """
        TREE MINIMUM recursive procedure

        Parameters
        ----------
        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        min : BinarySearchTree.Node
            Returns a pointer to the minimum element
            in the subtree rooted at a given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x is None:
            x = self._root

        if not x.left.isnil():
            return self.recursive_tree_minimum(x.left)
        else:
            return x

    def recursive_tree_maximum(self, x=None):
        """
        TREE MAXIMUM recursive procedure

        Returns a pointer to the maximum element in
        the subtree rooted at a given node x.

        Parameters
        ----------
        x : BinarySearchTree.Node, default=None
            Given node x. If not provided, it will default to
            starting the root of the entire tree.

        Returns
        -------
        max : BinarySearchTree.Node
            Returns a pointer to the maximum element
            in the subtree rooted at a given node x.

        Notes
        -----
        CLRS Exercises 12.2-2.

        """
        if x is None:
            x = self._root

        if not x.right.isnil():
            return self.recursive_tree_maximum(x.right)
        else:
            return x

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

        Returns
        -------
        succ : BinarySearchTree.Node
            Returns a pointer to the successor element
            in the subtree rooted at a given node x.

        """
        if not x.right.isnil():
            return self.tree_minimum(x.right)
        y = x.p
        while not y.isnil() and x is y.right:
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

        Returns
        -------
        pred : BinarySearchTree.Node
            Returns a pointer to the predecessor element
            in the subtree rooted at a given node x.

        """
        if not x.left.isnil():
            return self.tree_maximum(x.left)
        y = x.p
        while not y.isnil() and x is y.left:
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
        y = self._NIL
        x = self._root
        while not x.isnil():
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        # set children to sentinel
        z.left = self._NIL
        z.right = self._NIL
        if y.isnil():
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
        if u.p.isnil():
            self._root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if not v.isnil():
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
        if z.left.isnil():
            self.transplant(z, z.right)
        elif z.right.isnil():
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
