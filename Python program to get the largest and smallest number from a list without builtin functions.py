# 2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

def find_largest_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = find_largest_smallest(numbers)
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")
