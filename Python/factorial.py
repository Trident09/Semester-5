def factorial(n):
 if n == 0 or n == 1:
     return 1
 else:
     return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
  print("factorial does not exist for", num)
else:
  print("The factorial of", num, "is", factorial(num))
