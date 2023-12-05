# Get the dimensions of the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Check if the matrices can be multiplied
if cols1 != rows2:
   print("The matrices cannot be multiplied.")
else:
   # Get the elements of the matrices from the user
   A = []
   for i in range(rows1):
       row = []
       for j in range(cols1):
           row.append(float(input(f"Enter element A{i+1}{j+1}: ")))
       A.append(row)

   B = []
   for i in range(rows2):
       row = []
       for j in range(cols2):
           row.append(float(input(f"Enter element B{i+1}{j+1}: ")))
       B.append(row)

   # Initialize a result matrix with zeros
   result = [[0 for _ in range(cols2)] for _ in range(rows1)]

   # Multiply the matrices
   for i in range(rows1):
       for j in range(cols2):
           for k in range(cols1):
               result[i][j] += A[i][k] * B[k][j]

   # Print the result matrix
   for r in result:
       print(r)
