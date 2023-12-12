import numpy as np
import array as arr

# Creating an array
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("The new created array is : ", end=" ")
for i in range(0, 6):
   print(a[i], end=" ")

# Accessing elements in an array
print("\nAccess element is: ", a[0])
print("Access element is: ", a[3])

# Slicing an array
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array('i', l)
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Updating elements in an array
arr = arr.array('i', [1, 2, 3, 1, 2, 5])
print("\nArray before updation : ", end="")
for i in range(0, 6):
   print(arr[i], end=" ")
arr[2] = 6
print("\r")
print("Array after updation : ", end="")
for i in range(0, 6):
   print(arr[i], end=" ")


# Basic array operations
data = np.array([1, 2, 3, 4, 5, 6])
ones = np.ones(6, dtype=int)
print("\nAddition: ", data + ones)
print("Subtraction: ", data - ones)
print("Multiplication: ", data * data)
print("Division: ", data / data)

# Summing elements in an array
a = np.array([1, 2, 3, 4])
print("\nSum of elements: ", a.sum())

# Selecting elements based on a condition
a = np.array([1, 2, 3, 4, 5, 6])
print("\nElements greater than 3: ", a[a > 3])

# Selecting elements based on multiple conditions
a = np.array([1, 2, 3, 4, 5, 6])
print("\nElements greater than 2 and less than 5: ", a[(a > 2) & (a < 5)])
