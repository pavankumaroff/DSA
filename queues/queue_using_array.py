class ArrayQueue:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def __repr__(self):
        return f"ArrayQueue(queue={self.items}, front={self.front}, rear={self.rear})"

    def enqueue(self, value):
        if self.isFull():
            raise OverflowError("enqueue to a full queue")

        else:
            self.items[self.rear] = value
            self.rear = (self.rear + 1) % len(self.items)

            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")

        item = self.items[self.front]
        self.items[self.front] = 0
        self.front = (self.front + 1) % len(self.items)

        self.count -= 1

        return item

    def isPeak(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")

        return self.items[self.front]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.items)

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        index = self.front

        for _ in range(self.count):
            print(self.items[index], end=" ")
            index = (index + 1) % len(self.items)


queue = ArrayQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(5)
queue.dequeue()
queue.dequeue()
# queue.dequeue()
# queue.dequeue()
queue.enqueue(12)


# print(queue)
queue.display()
