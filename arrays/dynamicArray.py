import math


class Array:
    def __init__(self, length):
        self.__items = [0] * length
        self.__count = 0

    def print(self):
        for i in range(self.__count):
            print(self.__items[i])

    def insert(self, item):
        if len(self.__items) == self.__count:
            new_items = [0] * (self.__count * 2)

            for index, value in enumerate(self.__items):
                new_items[index] = value

            self.__items = new_items

        self.__items[self.__count] = item
        self.__count += 1

    def removeAt(self, index):
        if (index < 0 or index >= self.__count):
            raise TypeError("Index out of range: list index is invalid.")

        for i in range(index, self.__count - 1):
            self.__items[i] = self.__items[i + 1]

        self.__count -= 1

    def indexOf(self, item):
        for i in range(self.__count):
            if (self.__items[i] == item):
                return i
        return -1

    def max(self):
        max_item = self.__items[0]
        index = 0
        while index <= self.__count:
            if max_item < self.__items[index]:
                max_item = self.__items[index]

            index += 1

        return max_item

    def reverse(self):
        left, right = 0, self.__count - 1
        while left < right:
            self.__items[left], self.__items[right] = self.__items[right], self.__items[left]
            left += 1
            right -= 1

    def insertAt(self, item, index):
        if (index < 0 or index > self.__count):
            raise TypeError("Index out of range: list index is invalid.")

        if len(self.__items) == self.__count:
            new_items = [0] * (self.__count * 2)

            for i, value in enumerate(self.__items):
                new_items[i] = value

            self.__items = new_items

        for i in range(self.__count, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = item

        self.__count += 1


array = Array(3)
array.insert(100)
array.insert(2)
array.insert(3000)
array.insert(4)
array.insert(500)
# array.insert(6)
# array.removeAt(5)
# array.removeAt(2)
# array.insertAt(100, 6)
# array.print()
array.reverse()
print(array.max())
# array.print()
# print(array.indexOf(5))
