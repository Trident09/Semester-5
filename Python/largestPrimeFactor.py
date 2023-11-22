def largest_prime_factor():
   n = int(input("Enter a number: "))
   m = n
   i = 2
   while i * i <= n:
       if n % i:
           i += 1
       else:
           n //= i
   print("The largest prime factor of", m, "is", n)

# Test the function
largest_prime_factor()
