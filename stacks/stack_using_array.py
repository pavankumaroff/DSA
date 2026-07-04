class InvalidOperationError(Exception):
    pass


class Stack:
    def __init__(self, value=5):
        self.__items = [0] * value
        self.__count = 0

    def push(self, item):
        if self.__count == len(self.__items):
            raise InvalidOperationError("stack over flow")

        self.__items[self.__count] = item
        self.__count += 1

    def pop(self):
        if self.__count == 0:
            raise InvalidOperationError("stack under flow")

        self.__count -= 1
        return self.__items[self.__count]

    def peek(self):
        if self.__count == 0:
            raise InvalidOperationError("stack under flow")

        return self.__items[self.__count - 1]

    def is_empty(self):
        return self.__count == 0

    def print(self):
        return self.__items[:self.__count]


stack = Stack(10)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())
