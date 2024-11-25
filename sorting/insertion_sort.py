# insertion sort

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


array = [2, 1, 6, 3, 4, 9, 5]
insertion_sort(array)
print(array)
