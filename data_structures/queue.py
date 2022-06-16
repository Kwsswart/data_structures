"""
Implementations of different types of queues.
"""
from abc import ABC, abstractmethod


class Queue(ABC):

    @abstractmethod
    def enqueue(self, item):
        """
        Insert element into queue.
        """

    @abstractmethod
    def dequeue(self):
        """
        Remove element from queue.
        """

    @abstractmethod
    def is_empty(self):
        """
        Check if queue is empty.
        """

    @abstractmethod
    def peek(self):
        """
        Return value of next value in queue without removing it.
        """


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
        return not self.queue

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]


class CircularQueue(Queue):

    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue = [None] * queue_size
        # Set front and rear to negative value, thus indicating empty queue.
        self.front, self.rear = -1, -1

    def increase_rear_index(self):
        """
        Circularly increase rear index by 1, if it reaches the end, then the next value would be the start of the queue.
        """
        return (self.rear + 1) % self.queue_size

    def increase_front_index(self):
        """
        Circularly increase front index by 1, if it reaches the end, then the next value would be the start of the queue
        """
        return (self.front + 1) % self.queue_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full.")
        elif self.front == -1:
            self.front, self.rear = 0, 0
            self.queue[self.rear] = item
        else:
            self.rear = self.increase_rear_index()
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        if self.front == self.rear:
            # return the singular value and reset it to an empty queue
            value = self.queue[self.front]
            self.front, self.rear = -1, -1
            return value
        value = self.queue[self.front]
        self.front = self.increase_front_index()
        return value

    def is_full(self):
        return self.increase_rear_index() == self.front

    def is_empty(self):
        return self.front == -1

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
