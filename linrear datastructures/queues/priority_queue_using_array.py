class PriorityQueue:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.count = 0

    def __str__(self):
        return f"{self.items}"

    def add(self, item):
        if self.isFull():
            raise OverflowError("adding item to full queue")

        index = -1

        # shifting items from left to right
        for i in range(self.count - 1, -1, -1):
            if (self.items[i] > item):
                self.items[i + 1] = self.items[i]
            else:
                index = i
                break

        self.items[index + 1] = item
        self.count += 1

    def remove(self):
        if self.isEmpty():
            raise IndexError("removing item from empty queue")

        item = self.items[self.count - 1]
        self.count -= 1

        return item

    def isFull(self):
        return self.count == len(self.items)

    def isEmpty(self):
        return self.count == 0


queue = PriorityQueue(5)
queue.add(5)
queue.add(3)
queue.add(2)
queue.add(4)
queue.add(1)
# queue.add(1)

while not queue.isEmpty():
    print(queue.remove())
