# Right-angled triangle
print('Right-angled triangle')
n = 5
for i in range(1, n+1):
  print('*' * i)

# Inverted right-angled triangle
print('Inverted right-angled triangle')
n = 5
for i in range(n, 0, -1):
 print('*' * i)

# Pyramid
print('Pyramid')
n = 5
for i in range(n):
  print(' ' * (n-i-1) + '*' * (2*i+1))
