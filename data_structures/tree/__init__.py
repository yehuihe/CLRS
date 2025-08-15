"""
=============================
Tree (:mod:`CLRS.tree`)
=============================

"""

from ._base import Tree, BinaryTree
from ._binary_search_tree import BinarySearchTree
from ._balance_search_tree import Color, RedBlackTree


__all__ = [s for s in dir() if not s.startswith("_")]

