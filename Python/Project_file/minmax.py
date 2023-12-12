# Ask the user to enter the elements of the list
n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
   num = int(input(f"Enter element {i+1}: "))
   lst.append(num)

# Find the smallest and largest numbers in the list
smallest = min(lst)
largest = max(lst)

# Print the smallest and largest numbers
print("The smallest number in the list is: ", smallest)
print("The largest number in the list is: ", largest)
