# linear search

def linear_search(array, target):
      n = len(array)

      for index in range(n):
          if (array[index] == target):
              return index
    
      return -1
  

array = [1, 2, 8, 4, 3, 6]
result = linear_search(array, 6)
print(result)