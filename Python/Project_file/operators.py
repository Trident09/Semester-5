# Logical Operators
print("Logical AND: ", True and False) # Output: False
print("Logical OR: ", True or False)  # Output: True
print("Logical NOT: ", not True)     # Output: False

# Bitwise Operators
a = 60 # 60 = 0011 1100 
b = 13 # 13 = 0000 1101
print("Bitwise AND: ", a & b)         # Output: 12 (0000 1100)
print("Bitwise OR: ", a | b)          # Output: 61 (0011 1101)
print("Bitwise NOT: ", ~a)            # Output: -61 (-0011 1101)
print("Bitwise XOR: ", a ^ b)         # Output: 49 (0011 0001)

# Membership Operators
print("a in [1, 2, 3]: ", 1 in [1, 2, 3]) # Output: True
print("a not in [1, 2, 3]: ", 4 not in [1, 2, 3]) # Output: True

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b: ", a is b) # Output: True
print("a is not c: ", a is not c) # Output: True
print("a is c: ", a is c) # Output: False
