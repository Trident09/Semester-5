# Taking user input for different data types and converting them

# Taking input for an integer
x = input("Enter an integer: ")
integer_value = int(x)
print("Integer value:", integer_value)
float_value = float(x)
print("Float value:", float_value)

# Taking input for a string
z = input("Enter a string: ")
print("String value:", z)

# Taking input for a list of integers
numbers = input("Enter a list of integers (space-separated): ")
integer_list = [int(num) for num in numbers.split()]
print("List of integers:", integer_list)

# Taking input for a dictionary
key = input("Enter a key for the dictionary: ")
value = input("Enter a value for the dictionary: ")
dictionary = {key: value}
print("Dictionary:", dictionary)
