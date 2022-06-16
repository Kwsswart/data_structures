"""
Implementation of the Stack Data Structure.
"""


class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_stack(self):
        return self.stack
