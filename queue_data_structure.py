from __future__ import annotations


class Node:
    def __init__(self, data: int = None, next: Node = None) -> None:
        self.data = data
        self.next = next


class Queue:

    head = None
    tail = None

    def add(self, data: int):
        node = Node(data=data)
        if self.tail != None:
            self.tail.next = node
        self.tail = node
        if self.head == None:
            self.head = node

    def is_empty(self):
        return self.head == None

    def remove(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail == None
        return data


q = Queue()
q.add(4)
q.add(3)
q.add(2)
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
