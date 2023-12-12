def is_geometric_progression(sequence):
  if len(sequence) < 2:
      return True
  else:
      ratio = sequence[1] / float(sequence[0])
      for index in range(2, len(sequence)):
          if not (sequence[index] / float(sequence[index - 1]) == ratio):
              return False
      return True

# Ask the user for a sequence of numbers
sequence = list(map(int, input("Enter a sequence of numbers separated by space: ").split()))

# Check if the sequence is a GP
if is_geometric_progression(sequence):
  print("The sequence is a Geometric Progression.")
else:
  print("The sequence is not a Geometric Progression.")
