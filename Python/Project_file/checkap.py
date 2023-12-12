def is_arithmetic_progression(sequence):
  if len(sequence) < 2:
      return True
  else:
      diff = sequence[1] - sequence[0]
      for index in range(len(sequence) - 1):
          if not (sequence[index + 1] - sequence[index] == diff):
              return False
      return True

# Ask the user for a sequence of numbers
sequence = list(map(int, input("Enter a sequence of numbers separated by space: ").split()))

# Check if the sequence is an AP
if is_arithmetic_progression(sequence):
   print("The sequence is an Arithmetic Progression.")
else:
   print("The sequence is not an Arithmetic Progression.")
