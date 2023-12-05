def is_perfect_square(number):
  if number < 0:
      return False
  sqrt = int(number ** 0.5)
  return sqrt * sqrt == number

num = int(input("Enter a number: "))
if is_perfect_square(num):
  print(str(num) + " is a perfect square.")
else:
  print(str(num) + " is not a perfect square.")
