"""
Complexity
A complexity of O(n) just means we need a number of jumps equal to the number of elements

O(n2) means we need up to 9 jumps to navigate a collection of 3 elements
O(log2n) means we need up to 3 jumps to navigate a collection of 7 elements
"""


class Queue:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head


class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items = [e] + self.items

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head


stack = Stack()
stack.push(10)
stack.push(15)
stack.push(20)
print(stack.pop())
print(stack.items)
