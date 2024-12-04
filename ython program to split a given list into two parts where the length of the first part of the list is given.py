# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.

#       Original list: [1, 1, 2, 3, 4, 4, 5, 1]

#       Length of the first part of the list: 3

#       Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1]) 

def split_list(input_list, length_first_part):
    first_part = input_list[:length_first_part]
    second_part = input_list[length_first_part:]
    return first_part, second_part

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part, second_part = split_list(original_list, length_of_first_part)

print(f"Original list: {original_list}")
print(f"Length of the first part of the list: {length_of_first_part}")
print(f"Splitted the said list into two parts: ({first_part}, {second_part})")
