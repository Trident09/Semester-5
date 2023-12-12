try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is", y)
finally:
    print("Finally block executed!")
