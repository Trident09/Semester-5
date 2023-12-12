def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
      swapped = False
      for j in range(0, n-i-1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
              swapped = True
      if not swapped:
          break
  return arr

# Taking user input for the list of numbers
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]

sorted_list = bubbleSort(input_list)
print("Sorted list:", sorted_list)
