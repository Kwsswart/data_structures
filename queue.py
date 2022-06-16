"""
Implementations of different types of queues.
"""
from abc import ABC, abstractmethod


class Queue(ABC):

    @abstractmethod
    def enqueue(self):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class SimpleQueue(Queue):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
