from abc import ABCMeta, abstractmethod
from enum import Enum

from data_structures.tree import BinarySearchTree

__all__ = ["Color", "RedBlackTree"]


class Color(Enum):
    RED = 1
    BLACK = 2


class BalanceSearchTree(BinarySearchTree, metaclass=ABCMeta):
    # _NIL = object()

    def _left_rotate(self, x):
        """LEFT-ROTATE procedure

        Rotation is a local operation in a search tree that preserves
        the binary-search-tree property. When we do a left rotation
        on a node x, we assume that its right child y is not T.nil; x may be any node in
        the tree whose right child is not T.nil. And that the
        root’s parent is T.nil.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        y = x.right  # set y
        x.right = y.left  # turn y’s left subtree into x’s right subtree
        if not y.left.isnil():
            y.left.p = x
        y.p = x.p  # link x’s parent to y
        if x.p.isnil():
            self._root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x  # put x on y’s left
        x.p = y

    def _right_rotate(self, x):
        """RIGHT-ROTATE procedure

        Symmetric to LEFT-ROTATE procedure.

        Parameters
        ----------
        x : BinarySearchTree.Node
            Given node x.

        """
        y = x.left
        x.left = y.right
        if not y.right.isnil():
            y.right.p = x
        y.p = x.p
        if x.p.isnil():
            self._root = y
        elif x is x.p.right:
            x.p.right.p = y
        else:
            x.p.left = y
        y.right = x
        x.p = y


class RedBlackTree(BalanceSearchTree):
    """
    Red Black Tree.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the RedBlackTree data structure is:

    Create a red black tree as Figure 13.3 in CLSR.

    >>> from data_structures.tree import Color, RedBlackTree

    Create a red black tree as Figure 13.4 in CLSR.

    # TODO: Tell user how to create a tree with correct insertion order.

    >>> from data_structures.tree import Color, RedBlackTree
    >>> rbt = RedBlackTree()
rbt.rb_insert(RedBlackTree.Node(11, color=Color.BLACK))
rbt.rb_insert(RedBlackTree.Node(2, color=Color.RED))
rbt.rb_insert(RedBlackTree.Node(14, color=Color.BLACK))
rbt.rb_insert(RedBlackTree.Node(1, color=Color.BLACK))
rbt.rb_insert(RedBlackTree.Node(7, color=Color.BLACK))
rbt.rb_insert(RedBlackTree.Node(15, color=Color.RED))
rbt.rb_insert(RedBlackTree.Node(5, color=Color.RED))
rbt.rb_insert(RedBlackTree.Node(8, color=Color.RED))

    Inserting an item with key 4 into a binary search tree in Case 1.

    >>> rbt.rb_insert(RedBlackTree.Node(4, color=Color.RED))



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


    """

    class Node(BinarySearchTree.Node):
        """
        The node of a red black tree T

        Each node of the tree now contains
        the attributes color, key, left, right, and p.

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

        color : Color, default: RED
            The color of this node. Which can be either RED or BLACK.

        Examples
        --------
        Create a node with key 6:

        >>> x = RedBlackTree.Node(6)
        >>> x
        BinarySearchTree.Node(key=6, left=None, right=None, p=None), address=0x1f0f7d8d540)

        """
        __slots__ = "color"

        def __init__(self, key, left=None, right=None, p=None, color=Color.RED):
            super().__init__(key, left, right, p)
            self.color = color

        def __repr__(self):
            return (f"{self.__class__.__qualname__}(key={self.key}, "
                    f"address={hex(id(self))}, "
                    f"color={self.color.name})")

        def isnil(self):
            return False

    class NIL(Node):
        """The sentinel"""
        def __init__(self):
            super().__init__("T.nil", color=Color.BLACK)
            self.left = self
            self.right = self
            self.p = self

        def isnil(self):
            return True

        def __repr__(self):
            return (f"{self.__class__.__qualname__}(color={self.color.name} "
                    f"address={hex(id(self))})")

    _NIL = NIL()  # The sentinel

    def __init__(self):
        super().__init__()
        self._root = self._NIL
        self._root.p = self._NIL
        self._n = 0

    def __setitem__(self, key, value):
        raise NotImplementedError("__setitem__ is not implemented")

    def __delitem__(self, key):
        z = self.tree_search(self._root, key)
        if z:
            self.rb_delete(z)

    def _black_height(self, x):
        black_height = 0
        while not x.left.isnil():
            x = x.left
            if x.color == Color.BLACK:
                black_height += 1
        return black_height + 1  # add 1 since T.nil is black

    def black_height(self, x=None):
        """
        Calculating black-height of the node.

        Parameters
        ----------
        x : RedBlackTree.Node
            Given node x.

        Returns
        -------
        bh : int
            Returns black-height of the node x.
            By property 5, the notion of black-height is well defined,
            since all descending simple paths from the node have
            the same number of black nodes.
            We define the black-height of a red-black tree to be the black-height of its root.

        """
        if not x:
            x = self._root
        return self._black_height(x)

    def rb_insert(self, z):
        """
        RB-INSERT procedure.

        To insert a new value v into a red black tree T.

        It modifies T and some of the attributes of z in such a way that
        it inserts z into an appropriate position in the tree.
        The procedures TREE-INSERT and RB-INSERT differ as
        to insert node z into the tree T as if it were an ordinary binary search tree,
        and then we color z red. To guarantee that the red-black properties are preserved, we
        then call an auxiliary procedure RB-INSERT-FIXUP to recolor nodes and perform
        rotations.

        Parameters
        ----------
        z : RedBlackTree.Node
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
        if y.isnil():
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self._NIL
        z.right = self._NIL
        z.color = Color.RED
        self._rb_insert_fixup(z)
        self._n += 1

    def _rb_insert_fixup(self, z):
        """
        RB-INSERT-FIXUP procedure.

        To restore the red-black properties.

        Parameters
        ----------
        z : RedBlackTree.Node
            The node z to fixup.

        """
        while z.p.color == Color.RED:
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color == Color.RED:
                    z.p.color = Color.BLACK  # case 1
                    y.color = Color.BLACK  # case 1
                    z.p.p.color = Color.RED  # case 1
                    z = z.p.p  # case 1
                else:
                    if z is z.p.right:
                        z = z.p  # case 2
                        self._left_rotate(z)  # case 2
                    z.p.color = Color.BLACK  # case 3
                    z.p.p.color = Color.RED  # case 3
                    self._right_rotate(z.p.p)  # case 3
            elif z.p is z.p.p.right:
                y = z.p.p.left
                if y.color == Color.RED:
                    z.p.color = Color.BLACK  # case 1
                    y.color = Color.BLACK  # case 1
                    z.p.p.color = Color.RED  # case 1
                    z = z.p.p  # case 1
                else:
                    if z is z.p.left:
                        z = z.p  # case 2
                        self._right_rotate(z)  # case 2
                    z.p.color = Color.BLACK  # case 3
                    z.p.p.color = Color.RED  # case 3
                    self._left_rotate(z.p.p)  # case 3
        self._root.color = Color.BLACK

    def rb_transplant(self, u, v):
        """
        Subroutine RB-TRANSPLANT

        Which replaces one subtree as a child of its
        parent with another subtree.

        Parameters
        ----------
        u : RedBlackTree.Node
            The subtree rooted at node u.

        v : RedBlackTree.Node
            The subtree rooted at node v.

        """
        if u.p.isnil():
            self._root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def rb_delete(self, z):
        """
        Deleting a node z from a red black tree T.

        # TODO: implement self._n size change.

        After deleting node z, RB-DELETE calls an auxiliary
        procedure RB-DELETE-FIXUP, which changes colors and performs rotations to
        restore the red-black properties.

        Parameters
        ----------
        z : RedBlackTree.Node
            The node z to delete.

        """
        y = z
        y_original_color = y.color
        if z.left.isnil():
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right.isnil():
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.left
            if y.p is z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self._rb_delete_fixup(x)

    def _rb_delete_fixup(self, x):
        """
        RB-DELETE-FIXUP procedure.

        To restore the red-black properties.

        Parameters
        ----------
        x : RedBlackTree.Node
            The node z to delete.

        """
        while not x.isnil() and x.color == Color.BLACK:
            if x is x.p.left:
                w = x.p.right
                if w.color == Color.RED:
                    w.color = Color.BLACK  # case 1
                    x.p.color = Color.RED  # case 1
                    self._left_rotate(x.p)  # case 1
                    w = x.p.right  # case 1
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED  # case 2
                    x = x.p  # case 2
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK  # case 3
                        w.color = Color.RED  # case 3
                        self._right_rotate(w)  # case 3
                        w = x.p.right  # case 3
                    w.color = x.p.color  # case 4
                    x.p.color = Color.BLACK  # case 4
                    w.right.color = Color.BLACK  # case 4
                    self._left_rotate(x.p)  # case 4
                    x = self._root  # case 4
            elif x is x.p.right:
                w = x.p.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self._right_rotate(x.p)
                    w = x.p.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.p)
                    x = self._root
        x.color = Color.BLACK

    def transplant(self, u, v):
        """
        Overriding BinarySearchTree.transplant with RedBlackTree.re_transplant.

        See rb_transplant for more details.
        """
        self.rb_transplant(u, v)

    def tree_insert(self, z):
        """
        Overriding BinarySearchTree.tree_insert with RedBlackTree.re_insert.

        See rb_insert for more details.
        """
        self.rb_insert(z)

    def tree_delete(self, z):
        """
        Overriding BinarySearchTree.tree_delete with RedBlackTree.re_delete.

        See rb_delete for more details.
        """
        self.rb_delete(z)




