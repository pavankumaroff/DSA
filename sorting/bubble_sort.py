# bubble sort

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    

array = [10, 2, 1, 5, 8, 4, 6, 3, 7, 9]
bubble_sort(array)
print(array)
