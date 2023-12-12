# Taking string input
str_input = input("Enter a string: ")
print("You entered: ", str_input)

# Taking integer input
try:
   int_input = int(input("Enter an integer: "))
   print("You entered: ", int_input)
except ValueError:
   print("That's not an integer!")

# Taking float input
try:
   float_input = float(input("Enter a float: "))
   print("You entered: ", float_input)
except ValueError:
   print("That's not a float!")

# Taking multiple inputs
try:
   multiple_inputs = list(map(float, input("Enter multiple floats separated by space: ").split()))
   print("You entered: ", multiple_inputs)
except ValueError:
   print("That's not a valid input!")
