from collections import deque

class Queue:
    def __init__(self):
        self.len =0
        self.front = 0
        self.rear = 0
        self.deq = deque()

    def push(self, value):
        self.rear += 1
        self.deq.append(value)
        self.len += 1

    def pop(self):
        self.front += 1
        self.deq.popleft()

