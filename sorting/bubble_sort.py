# bubble sort

def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break


array = [10, 2, 1, 5, 8, 4, 6, 3, 7, 9]
bubble_sort(array)
print(array)
