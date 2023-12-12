# Using a for loop
print("Using a for loop")
for i in range(10):
   print(i)

# Using a while loop
print("Using a while loop")
i = 0
while i < 10:
   print(i)
   i += 1

# Using nested loops
print("Using nested loops")
for i in range(1, 6):
   for j in range(1, i+1):
       print(j, end=" ")
   print()
