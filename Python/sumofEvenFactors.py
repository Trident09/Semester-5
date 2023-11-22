def sum_of_even_factors():
 n = int(input("Enter a number: "))
 s = 0
 factors = []
 for i in range(1, n+1):
     # Check if i is a factor of n
     if n % i == 0:
         # Check if i is even
         if i % 2 == 0:
             # Add i to the sum
             s += i
             # Add i to the list of factors
             factors.append(i)
 print("The sum of the even factors of", n, "is", s)
 print("The even factors are", factors)

# Test the function
sum_of_even_factors()
