#A python program to create a regex to retrieve

import re

print("Enter the text")
text = input()

# All words having at least 4 characters
result_1 = re.findall(r'\b\w{4,}\b', text)

# All words having 3, 4, or 5 characters
result_2 = re.findall(r'\b\w{3,5}\b', text)

# Only simple digit numbers from a string
result_3 = re.findall(r'\b\d+\b', text)

# All words having 5 characters length
result_4 = re.findall(r'\b\w{5}\b', text)

# All word starting with a numeric digit 
result_5 = re.findall(r'\b[0-9]\w+\b', text)

# All words starting with 'a' in a given string
result_6 = re.findall(r'\ba\w+\b', text)

# The phone number of a person
result_7 = re.findall(r'\b\d{10}\b', text)

print("All words having at least 4 characters \n",result_1)
print("All words having 3, 4, or 5 characters \n",result_2)
print("Only simple digit numbers from a string \n",result_3)
print("All words having 5 characters length \n",result_4)
print("All word starting with a numeric digit \n",result_5)
print("All words starting with 'a' in a given string \n", result_6)
print("The phone number of a person \n", result_7)
