class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        return f"{self.stack2[::-1] + self.stack1}"

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peak(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")

        if len(self.stack2) > 0:
            return self.stack2[-1]

        return self.stack1[0]

    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.enqueue(5)
# queue.enqueue(6)
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()

print(queue)
