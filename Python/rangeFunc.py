start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
step = int(input("Enter the step value: "))

# Range assignment operator: =
r = range(start, stop, step)
print("r =", list(r))

# Slice assignment operator: =
s = r[2:6]
print("s =", list(s))

# Length assignment operator: len()
length = len(r)
print("length =", length)

# Minimum assignment operator: min()
minimum = min(r)
print("minimum =", minimum)

# Maximum assignment operator: max()
maximum = max(r)
print("maximum =", maximum)

# Sum assignment operator: sum()
total = sum(r)
print("total =", total)
