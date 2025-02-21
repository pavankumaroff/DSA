class InvalidOperationError(Exception):
    pass


class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addLast(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addFirst(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def removeFirst(self):
        if not self.head:
            raise InvalidOperationError("linked list is empty")

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
        self.size -= 1

    def removeLast(self):
        if not self.head:
            raise InvalidOperationError("linked list is empty")

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current:
                if current.next == self.tail:
                    break
                current = current.next

            current.next = None
            self.tail = current
        self.size -= 1

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

    def list(self):
        items = [0] * self.size
        index = 0
        current = self.head
        while current:
            items[index] = current.value
            current = current.next
            index += 1
        return items

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def get_kth_from_the_end(self, k):
        if self.head == None:
            return

        first = self.head
        second = self.head
        for i in range(k - 1):
            second = second.next
            if not second:
                raise InvalidOperationError("value is out of range")

        while second is not self.tail:
            first = first.next
            second = second.next

        return first.value

    def reverse(self):
        if not self.head:
            return

        prev = self.head
        current = prev.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.tail = self.head
        self.tail.next = None
        self.head = prev


ll = LinkedList()
ll.addLast(10)
ll.addLast(20)
ll.addLast(30)
ll.addLast(40)
ll.addLast(50)
ll.addLast(60)
# ll.reverse()
# print(ll.size)
# ll.display()
print(ll.get_kth_from_the_end(11))
# print(ll.list())

# 100        101        102
# [1|101] -> [2|102] -> [3|None]

# 100        101        102
# [1|101] <- [2|100]  [3|None]
