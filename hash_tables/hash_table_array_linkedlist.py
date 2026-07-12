from linkedlist.singleLinkedlist import LinkedList


class InvalidOperationError(Exception):
    pass


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, capacity=5):
        self.entries = [None] * capacity
        self.size = 0

    def __hash(self, key):
        return hash(key) % len(self.entries)

    def put(self, key, value):
        index = self.__hash(key)

        if self.entries[index] is None:
            self.entries[index] = LinkedList()

        bucket = self.entries[index]

        # Update existing key
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        # Insert new key
        bucket.addLast(Entry(key, value))
        self.size += 1

    def get(self, key):
        index = self.__hash(key)
        bucket = self.entries[index]

        if bucket is None:
            return None

        for entry in bucket:
            if entry.key == key:
                return entry.value

        return None

    def remove(self, key):
        index = self.__hash(key)
        bucket = self.entries[index]

        if bucket is None:
            raise InvalidOperationError("Key not found.")

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                self.size -= 1
                return

        raise InvalidOperationError("Key not found.")

    def contains_key(self, key):
        return self.get(key) is not None

    def keys(self):
        result = []

        for bucket in self.entries:
            if bucket is not None:
                for entry in bucket:
                    result.append(entry.key)

        return result

    def values(self):
        result = []

        for bucket in self.entries:
            if bucket is not None:
                for entry in bucket:
                    result.append(entry.value)

        return result

    def items(self):
        result = []

        for bucket in self.entries:
            if bucket is not None:
                for entry in bucket:
                    result.append((entry.key, entry.value))

        return result

    def clear(self):
        self.entries = [None] * len(self.entries)
        self.size = 0

    def display(self):
        for index, bucket in enumerate(self.entries):
            print(f"Bucket {index}:", end=" ")

            if bucket is None:
                print("None")
                continue

            for entry in bucket:
                print(f"[{entry.key}: {entry.value}]", end=" -> ")

            print("None")

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.contains_key(key)


table = HashTable(5)

table.put(1, "Pavan")
table.put(6, "Raghu")
table.put(11, "Ram")
table.put(2, "Python")

table.display()
