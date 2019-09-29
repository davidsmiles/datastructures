from binarytree import BinaryTree
from node import Node

tree = BinaryTree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

[tree.add(Node(n)) for n in nodes]

tree.delete(9)
tree.inorder()

