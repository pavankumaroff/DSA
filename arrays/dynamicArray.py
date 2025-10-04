class Array:
    def __init__(self, length):
        self.__items = [0] * length
        self.__count = 0

    def print(self):
        for i in range(self.__count):
            print(self.__items[i])

    def append(self, item):
        if len(self.__items) == self.__count:
            newItems = [0] * (self.__count * 2)

            for index, value in enumerate(self.__items):
                newItems[index] = value

            self.__items = newItems

        self.__items[self.__count] = item
        self.__count += 1

    def pop(self, index):
        for i in range(index, self.__count - 1):
            self.__items[i] = self.__items[i + 1]

        self.__count -= 1


array = Array(3)
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)
array.append(6)
array.pop(1)
array.pop(0)
array.append(10)
array.print()
