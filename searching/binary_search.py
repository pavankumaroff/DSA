# binary search

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (array[mid] == target):
            return mid

        if (array[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
  
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(array, 4)
print(result)
