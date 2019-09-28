"""
implementing binary tree algorithm, adding new node
and recursively going over the binary tree
"""
from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head

        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with this value exists.')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def _inorder_recursive(self, current_node: Node):
        """
        Inorder Traversal Binary Tree
        :param current_node:
        :return:
        """

        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def inorder(self):
        self._inorder_recursive(self.head)

    def _preorder_recursive(self, current_node: Node):
        """
        Preorder Traversal Binary Tree
        :param current_node:
        :return:
        """

        if not current_node:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

    def preorder(self):
        self._preorder_recursive(self.head)

