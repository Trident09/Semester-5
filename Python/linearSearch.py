def linear_search(arr, target):
   for index, item in enumerate(arr):
       if item == target:
           return index
   return -1

arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter the target value: "))

index = linear_search(arr, target)

if index != -1:
   print(f"'{target}' found at index {index}.")
else:
   print(f"'{target}' not found in the list.")
