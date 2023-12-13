# Create two matrices
A <- matrix(c(10, 8, 5, 12), ncol = 2, byrow = TRUE)
B <- matrix(c(5, 3, 15, 6), ncol = 2, byrow = TRUE)

# Print the matrices
print(A)
print(B)

# Addition
print("Addition:")
print(A + B)

# Subtraction
print("Subtraction:")
print(A - B)

# Transpose
print("Transpose of A:")
print(t(A))
print("Transpose of B:")
print(t(B))

# Matrix multiplication
print("Matrix multiplication:")
print(A %*% B)

# Power of a matrix
# You need to install the 'expm' package for this operation
# install.packages("expm")
# library(expm)
# print("Power of A:")
# print(A %^% 2)