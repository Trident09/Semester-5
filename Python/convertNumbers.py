# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = 0
    power = 0
    while decimal != 0:
        binary += (decimal % 2) * (10 ** power)
        decimal //= 2
        power += 1
    return binary

# Function to convert octal to decimal
def octal_to_decimal(octal):
    decimal = 0
    power = 0
    while octal != 0:
        decimal += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1
    return decimal

# Function to convert decimal to octal
def decimal_to_octal(decimal):
    octal = 0
    power = 0
    while decimal != 0:
        octal += (decimal % 8) * (10 ** power)
        decimal //= 8
        power += 1
    return octal

# Function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for digit in hexadecimal[::-1]:
        if digit.isalpha():
            decimal += hex_map[digit.upper()] * (16 ** power)
        else:
            decimal += int(digit) * (16 ** power)
        power += 1
    return decimal

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while decimal != 0:
        remainder = decimal % 16
        if remainder > 9:
            hexadecimal = hex_map[remainder] + hexadecimal
        else:
            hexadecimal = str(remainder) + hexadecimal
        decimal //= 16
    return hexadecimal

# Taking user input
number = input("Enter the number: ")
base = input("Enter the base of the number (binary, octal, hexadecimal, decimal): ")

# Converting the number based on the given base
if base == "binary":
    decimal = binary_to_decimal(int(number))
    octal = decimal_to_octal(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)
elif base == "octal":
    decimal = octal_to_decimal(int(number))
    binary = decimal_to_binary(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)
elif base == "hexadecimal":
    decimal = hexadecimal_to_decimal(number)
    binary = decimal_to_binary(decimal)
    octal = decimal_to_octal(decimal)
elif base == "decimal":
    binary = decimal_to_binary(int(number))
    octal = decimal_to_octal(int(number))
    hexadecimal = decimal_to_hexadecimal(int(number))

# Displaying the converted numbers
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
