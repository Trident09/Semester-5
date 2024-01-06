import array as arr


def find_elements(arr):
    # Initialize variables
    largest = None
    second_largest = None
    smallest = None
    second_smallest = None

    # Iterate over the array
    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest and num != largest:
            second_largest = num

        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest


# Ask the user to enter the elements of the array
elements = list(
    map(int, input("Enter the elements of the array, separated by spaces: ").split())
)

# Convert the list to an array
arr = arr.array("i", elements)

# Call the function
second_largest, second_smallest = find_elements(arr)

print("Second largest element is: ", second_largest)
print("Second smallest element is: ", second_smallest)
