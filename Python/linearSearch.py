def linear_search(arr, search):
   for index, item in enumerate(arr):
       if item == search:
           return index
   return -1

arr = list(map(int, input("Enter elements with space between them: ").split()))
search = int(input("Enter the SEARCH value: "))

index = linear_search(arr, search)

if index != -1:
   print(f"'{search}' found at index {index}.")
else:
   print(f"'{search}' not found in the list.")
