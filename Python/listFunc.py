a = list(input("Enter the elements of list a (space-separated): ").split())
b = list(input("Enter the elements of list b (space-separated): ").split())

# Concatenation assignment operator: +=
c = a.copy()
c += b
print("c =", c)

# Repetition assignment operator: *=
c = a.copy()
c *= 3
print("c =", c)

# Append assignment operator: +=
c = a.copy()
c.append("x")
print("c =", c)

# Extend assignment operator: +=
c = a.copy()
c.extend(b)
print("c =", c)

# Insert assignment operator: insert()
c = a.copy()
c.insert(2, "x")
print("c =", c)

# Remove assignment operator: remove()
c = a.copy()
c.remove("x")
print("c =", c)

# Pop assignment operator: pop()
c = a.copy()
c.pop(2)
print("c =", c)

# Clear assignment operator: clear()
c = a.copy()
c.clear()
print("c =", c)
