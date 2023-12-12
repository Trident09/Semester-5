# A python program to search for city name in the file and display
# the record number that contains the city name.
with open('cities.txt', 'r') as f:
    city = input("Enter city name: ")
    record_number = 0
    flag = False
    for line in f:
        record_number += 1
        if city in line:
            print(f"{city} is in record number {record_number}")
            flag = True
            break
    if not flag:
      print("City not found!")