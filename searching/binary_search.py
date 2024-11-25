# binary search

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while (low <= high):
        mid = (low + high) // 2

        if (array[mid] == target):
            return mid

        if (array[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
  
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(array, 4)
print(result)
