class CircularQueue:
    def __init__(self, cap=5):
        self.data = [None] * cap
        self.size = 0
        self.front = 0

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Exception("queue empty")
        return self.data[self.front]

    def enqueue(self, val):
        if self.size == len(self.data):
            raise Exception("queue full")
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = val
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue empty")
        ans = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return ans

q = CircularQueue(4)
q.enqueue(5)
q.enqueue(12)
q.enqueue(19)
print("deq:", q.dequeue())
q.enqueue(25)
q.enqueue(31)
print("first:", q.first())
print("array:", q.data)
