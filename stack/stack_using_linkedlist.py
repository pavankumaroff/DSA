class InvalidOperationError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise InvalidOperationError("stack is under flow")

        popped_data = self.head.value
        self.head = self.head.next

        return popped_data

    def is_empty(self):
        return not self.head

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("stack is under flow")

        return self.head.value

    def display(self):
        current = self.head

        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
