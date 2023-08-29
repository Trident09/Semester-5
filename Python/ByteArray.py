# Function to create a byte array from a string
def create_byte_array_from_string(input_string):
    byte_array = bytes(input_string, 'utf-8')
    return byte_array

# Function to create a byte array from a list of integers
def create_byte_array_from_list(input_list):
    byte_array = bytes(input_list)
    return byte_array

# Function to create a byte array from a hexadecimal string
def create_byte_array_from_hex_string(hex_string):
    byte_array = bytes.fromhex(hex_string)
    return byte_array

# Taking user input for different types of byte arrays
string_input = input("Enter a string to create a byte array: ")
list_input = input("Enter a list of integers (space-separated) to create a byte array: ")
hex_input = input("Enter a hexadecimal string to create a byte array: ")

# Creating byte arrays based on the user input
byte_array_string = create_byte_array_from_string(string_input)
byte_array_list = create_byte_array_from_list([int(num) for num in list_input.split()])
byte_array_hex = create_byte_array_from_hex_string(hex_input)

# Displaying the created byte arrays
print("Byte array from string:", byte_array_string)
print("Byte array from list:", byte_array_list)
print("Byte array from hexadecimal string:", byte_array_hex)