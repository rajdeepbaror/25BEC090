class CircularDeque:
    def __init__(self, cap=6):
        self.data = [None] * cap
        self.size = 0
        self.front = 0

    def add_first(self, val):
        if self.size == len(self.data):
            raise Exception("deque full")
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = val
        self.size += 1

    def add_last(self, val):
        if self.size == len(self.data):
            raise Exception("deque full")
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = val
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise Exception("deque empty")
        ans = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return ans

    def delete_last(self):
        if self.size == 0:
            raise Exception("deque empty")
        back = (self.front + self.size - 1) % len(self.data)
        ans = self.data[back]
        self.data[back] = None
        self.size -= 1
        return ans

dq = CircularDeque(5)
dq.add_last(10)
dq.add_first(5)
dq.add_last(20)
print("del first:", dq.delete_first())
print("del last:", dq.delete_last())
print("remaining:", dq.data)
