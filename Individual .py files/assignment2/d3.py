class Node:
    def __init__(self, elem, nxt=None):
        self.elem = elem
        self.nxt = nxt

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, val):
        newest = Node(val, self.head)
        self.head = newest
        if self.size == 0:
            self.tail = newest
        self.size += 1

    def insert_last(self, val):
        newest = Node(val, None)
        if self.size == 0:
            self.head = newest
        else:
            self.tail.nxt = newest
        self.tail = newest
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise Exception("list empty")
        val = self.head.elem
        self.head = self.head.nxt
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return val

    def traverse(self):
        cur = self.head
        out = []
        while cur is not None:
            out.append(cur.elem)
            cur = cur.nxt
        return out

sll = SinglyLinkedList()
sll.insert_first(20)
sll.insert_first(10)
sll.insert_last(30)
print("list:", sll.traverse())
print("deleted:", sll.delete_first())
print("after delete:", sll.traverse())
