class invalidOperationError(Exception):
    pass


class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addFirst(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def indexof(self, item):
        current = self.head
        index = 0

        while current:
            if current.value == item:
                return index
            current = current.next
            index += 1

        return -1

    def contains(self, item):
        return self.indexof(item) != -1

    def removeFirst(self):
        if not self.head:
            raise invalidOperationError("linked list is empty")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        temp = self.head.next
        self.head.next = None
        self.head = temp

    def removeLast(self):
        if not self.head:
            raise invalidOperationError("linked list is empty")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        prevous = self.head
        current = self.head.next

        while current.next:
            prevous = current
            current = current.next
        
        prevous.next = None
        self.tail = prevous

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.addLast(10)
ll.addLast(20)
ll.addLast(30)
# ll.addFirst(40)
# ll.addFirst(50)
# ll.removeFirst()
ll.removeLast()

ll.display()
