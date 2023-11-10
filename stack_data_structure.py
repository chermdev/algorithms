from __future__ import annotations


class Node:
    def __init__(self,
                 data: int = None,
                 next: Node = None) -> None:
        self.data = data
        self.next = next


class Stack:

    top = None

    def is_empty(self) -> bool:
        return self.top == None

    def peek(self) -> int:
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def push(self, data: int) -> None:
        node = Node(data=data)
        node.next = self.top
        self.top = node

    def pop(self) -> int:
        if self.is_empty():
            return "Stack is empty"
        data = self.top.data
        self.top = self.top.next
        return data


s = Stack()
s.push(5)
s.push(3)
s.push(2)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
