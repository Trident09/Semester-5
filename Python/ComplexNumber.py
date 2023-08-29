# Define a function to add two complex numbers
def complex_addition(num1, num2):
    return num1 + num2

# Define a function to subtract two complex numbers
def complex_subtraction(num1, num2):
    return num1 - num2

# Read the two complex numbers from the user
real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))
num1 = complex(real1, imaginary1)

real2 = float(input("Enter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))
num2 = complex(real2, imaginary2)

# Call the two functions with the two complex numbers as arguments
addition = complex_addition(num1, num2)
subtraction = complex_subtraction(num1, num2)

# Print the results
print("Addition is:", addition)
print("Subtraction is:", subtraction)

a = complex(input("kjsgksh"))