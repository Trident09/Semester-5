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
