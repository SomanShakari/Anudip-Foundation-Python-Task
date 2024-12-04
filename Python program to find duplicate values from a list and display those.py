# 3. Write a Python program to find duplicate values from a list and display those. 

def find_duplicates(numbers):
    duplicates = []
    seen = set()
    
    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        seen.add(number)
    
    return duplicates

numbers = [1, 2, 3, 4, 2, 5, 3, 6, 7, 3]
duplicates = find_duplicates(numbers)
print(f"The duplicate values in the list are: {duplicates}")
