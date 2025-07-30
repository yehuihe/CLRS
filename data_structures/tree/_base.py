from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping

from data_structures import Stack
from utils import ReadOnly


class Tree(MutableMapping, metaclass=ABCMeta):
    """Base class for all trees in CLRS."""

    root = ReadOnly()

    def __init__(self):
        self._root = None

    @staticmethod
    @abstractmethod
    def n_children(x):
        """
        Number of children node x has.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        n_children : int
            Number of children.

        """
        ...

    @staticmethod
    @abstractmethod
    def children(x):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @staticmethod
    def isleaf(x):
        """
        Check if a node is a tree leaf.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        leaf : bool
            Returns True if node is a leaf.

        """
        return Tree.n_children(x) == 0

    def isroot(self, x):
        """
        Check if a node is a tree root.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        root : bool
            Returns True if node is a root.

        """
        return self._root == x

    def isempty(self):
        """
        Check if the tree is empty.

        Returns
        -------
        empty : bool
            Returns True if tree is empty.

        """
        return len(self) == 0

    def depth(self, x):
        """
        Return the depth of a node.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        depth : int
            Returns depth of a node.

        """
        if self.isroot(x):
            return 0
        else:
            return 1 + self.depth(self.parent(x))

    def _height(self, x):
        if self.isleaf(x):
            return 0
        else:
            return 1 + max(self._height(child) for child in self.children(x))

    def height(self, x=None):
        """
        Return the height of the subtree rooted at x.

        If x is None, return the geight of the entire tree.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        height : int
            Returns height of the subtree rooted at x.

        """
        if not x:
            x = self._root
        return self._height(x)

    @staticmethod
    def preorder_tree_walk(x):
        """Preorder tree walk recursive procedure

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Yields
        ------
        preorder_walk : int
            Yields the root before the values in either subtree.

        """
        if x:
            yield x.key
            yield from Tree.preorder_tree_walk(x.left)
            yield from Tree.preorder_tree_walk(x.right)

    @staticmethod
    def postorder_tree_walk(x):
        """Postorder tree walk recursive procedure

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Yields
        ------
        postorder_walk : int
            Yields the root after the values in its subtrees.

        """
        if x:
            yield from Tree.postorder_tree_walk(x.left)
            yield from Tree.postorder_tree_walk(x.right)
            yield x.key

    # def tree_walk(self, order="preorder"):
    #     if order == "preorder":
    #         return self.preorder_tree_walk(self._root)
    #     else:
    #         return self.postorder_tree_walk(self._root)

    def __iter__(self):
        yield from self.preorder_tree_walk(self._root)


class BinaryTree(Tree, metaclass=ABCMeta):
    """Base class for binary trees in CLRS."""

    root = ReadOnly()
    n = ReadOnly()

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
                    # f"left={self.left}, "
                    # f"right={self.right}, "
                    # f"p={self.p}), "
                    f"address={hex(id(self))})")

        def __eq__(self, other):
            return other is self

        def __ne__(self, other):
            """Return True if other does not represent the same Node"""
            return not (self == other)

    def __init__(self):
        super().__init__()
        self._n = 0

    def __len__(self):
        """Return the total number of nodes in the tree"""
        return self._n

    @staticmethod
    def n_children(x):
        """
        Number of children node x has.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        n_children : int
            Number of children.

        """
        children = 0
        if x.left:
            children += 1
        if x.right:
            children += 1
        return children

    @staticmethod
    def sibling(x):
        """
        Return siblings of node x.

        Parameters
        ----------
        x : Tree.Node
            Given node x.

        Returns
        -------
        sibling : int
            Number of children.

        """
        if not x.p:  # Tree T was empty.
            return None
        else:
            if x == x.p.left:
                return x.p.right
            else:
                return x.p.left

    @staticmethod
    def children(x):
        """
        Generate children of node x.

        Parameters
        ----------
        x : BinaryTree.Node
            Given node x.

        Yields
        ------
        children : BinaryTree.Node
            Yields children of node x.

        """
        if x.left:
            yield x.left
        if x.right:
            yield x.right

    @staticmethod
    def inorder_tree_walk(x):
        """Inorder tree walk recursive procedure

        Parameters
        ----------
        x : BinaryTree.Node
            Given node x.

        Yields
        ------
        inorder_walk : int
             The key of the root of a subtree between yielding the values in its left subtree
            and yielding those in its right subtree.

        """
        if x:
            yield from BinaryTree.inorder_tree_walk(x.left)
            yield x.key
            yield from BinaryTree.inorder_tree_walk(x.right)

    @staticmethod
    def iterative_inorder_tree_walk(x):
        """Inorder tree walk iterative procedure

        # TODO: order is still wrong
        It yields the key of the root of a subtree
        between yielding the values in its left subtree
        and yielding those in its right subtree.

        Parameters
        ----------
        x : BinaryTree.Node
            Given node x.

        Yields
        ------
        inorder_walk : int
             The key of the root of a subtree between yielding the values in its left subtree
            and yielding those in its right subtree.

        """
        s = Stack(20)
        s.push(x)
        while not s.stack_empty():
            z = s.pop()
            if z:
                yield z.key
                s.push(z.right)
                s.push(z.left)

    def __iter__(self):
        yield from self.inorder_tree_walk(self._root)
