'''
You have data related to the number of daily visitor for a week. Your task id to perform data analysis using arrays.
1. Create an array named daily_visitors to store the number of daily visitors for a week: [1200, 1400, 1100, 1500, 1300, 1250, 1550]
2. Calculate and print the average daily visitors for the week.
3. Determine and print the days when the number of visitors exceeded the weekly average.
'''

from array import array

visitor = list(map(int, input("Enter the visitor count with space: ").split()))
visitor_array = array("i", visitor)

for i, v in enumerate(visitor_array, start=1):
    print(f"Day {i}: {v}")

total = sum(visitor_array)
average = round(total / len(visitor_array), 2)
print(f"Average visitors per day: {average}")

for i, v in enumerate(visitor_array, start=1):
    if v > average:
        print(f"Day {i} had {int(v - average)} more visitors than the average")
