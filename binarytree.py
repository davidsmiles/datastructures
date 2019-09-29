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
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find_node(self, value: int) -> Node:
        current_node = self.head

        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise LookupError(f'Node with {value} was not found.')

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            #   if you are looking to delete the head, checking the children won't give us the head
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find_node(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)

            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
            rightmost.right = to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = rightmost
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = rightmost
            else:
                self.head = rightmost
        elif to_delete.left or to_delete.right:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.right or to_delete.left
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
                self.head = to_delete.right or to_delete.left
        else:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None

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

    def _postorder_recursive(self, current_node: Node):
        """
        Postrder Traversal Binary Tree
        :param current_node:
        :return:
        """

        if not current_node:
            return
        self._postorder_recursive(current_node.left)
        self._postorder_recursive(current_node.right)
        print(current_node)

    def postorder(self):
        self._postorder_recursive(self.head)
