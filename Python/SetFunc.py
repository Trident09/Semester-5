a = set(input("Enter the elements of set a (space-separated): ").split())
b = set(input("Enter the elements of set b (space-separated): ").split())

# Union assignment operator: |=
c = a.copy()
c |= b
print("c =", c)

# Intersection assignment operator: &=
c = a.copy()
c &= b
print("c =", c)

# Difference assignment operator: -=
c = a.copy()
c -= b
print("c =", c)

# Symmetric difference assignment operator: ^=
c = a.copy()
c ^= b
print("c =", c)
