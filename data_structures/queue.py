"""
Implementations of different types of queues.

SimpleQueue - Standard implementation of First In First Out Queue.
CircularQueue - Implementation of a circular queue where the last element points to the first, linking it.
PriorityQueue - Implementation of a Priority Queue using the max-heap implementation.
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
            return None
        elif self.front == -1:
            self.front, self.rear = 0, 0
            self.queue[self.rear] = item
        else:
            self.rear = self.increase_rear_index()
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
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


class PriorityQueue(Queue):
    FRONT_OF_QUEUE_INDEX = 1

    def __init__(self, queue_size):
        self.max_queue_size = queue_size
        self.current_queue_size = 0
        self.queue = [None] * (queue_size + 1)

    def heapify(self, index):
        # Check that it is not the root node.
        if not self.check_if_leaf_node(index):

            # Check to see if the root is smaller than any of it's children
            if self.queue[index] < self.queue[self.get_left_child_index(index)] or \
                    self.queue[index] < self.queue[self.get_right_child_index(index)]:

                # if the root node is smaller than either child, check which child is the largest and swap the
                # root node with that node.
                if self.queue[self.get_left_child_index(index)] > self.queue[self.get_right_child_index(index)]:
                    self.swap_nodes(index, self.get_left_child_index(index))
                    self.heapify(self.get_left_child_index(index))

                else:
                    self.swap_nodes(index, self.get_right_child_index(index))
                    self.heapify(self.get_right_child_index(index))

    def enqueue(self, item):

        if self.is_full():
            return None

        self.current_queue_size += 1
        self.queue[self.current_queue_size] = item

        current_index = self.current_queue_size

        while self.queue[current_index] > self.queue[self.get_parent_index(current_index)]:
            self.swap_nodes(current_index, self.get_parent_index(current_index))
            current_index = self.get_parent_index(current_index)

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.queue[self.FRONT_OF_QUEUE_INDEX]

        self.queue[self.FRONT_OF_QUEUE_INDEX] = self.queue[self.current_queue_size]
        self.current_queue_size -= 1
        self.heapify(self.FRONT_OF_QUEUE_INDEX)

        return value

    def is_empty(self):
        return all(item is None for item in self.queue)

    def is_full(self):
        return self.current_queue_size >= self.max_queue_size

    def peek(self):
        return self.queue[self.FRONT_OF_QUEUE_INDEX]

    def check_if_leaf_node(self, index):
        if (self.current_queue_size // 2) <= index <= self.current_queue_size:
            return True
        return False

    def swap_nodes(self, root_node, child_node):
        """
        If the root node is smaller than either child, check which child is the largest and swap the root node with that
         node. This way the root will always be the highest element (lowest index) in the list.
        """
        self.queue[root_node], self.queue[child_node] = self.queue[child_node], self.queue[root_node]

    @staticmethod
    def get_parent_index(index):
        """
        Return the index of the parent for the node at the index
        """
        return index // 2

    @staticmethod
    def get_left_child_index(index):
        """
        Return the index of the left child for the node at the index
        """
        return 2 * index

    @staticmethod
    def get_right_child_index(index):
        """
        Return the index of the right child for the node at the index
        """
        return (2 * index) + 1
