"""
Deque (Double ended queue) - Implementation of a Circular Deque where insertion and removal of elements can either be
                    done from the front or the rear. Thus, it does not follow FIFO rule (First In First Out).
"""


class Deque:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def add_to_rear(self, item):
        self.queue.append(item)

    def add_to_front(self, item):
        self.queue.insert(0, item)

    def remove_from_rear(self):
        return self.queue.pop()

    def remove_from_front(self):
        return self.queue.pop(0)

