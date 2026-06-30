numbers = [1, 5, 9, 3, 2, 6, 7]


def sort():
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


sort()

print(numbers)
