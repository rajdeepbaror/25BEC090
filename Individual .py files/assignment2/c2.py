class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self.data.pop()

st = Stack()
st.push(10)
st.push(20)
print("top:", st.top())
print("pop:", st.pop())
print("len:", len(st))

try:
    st.pop()
    st.pop()
except Empty as e:
    print("error:", e)
