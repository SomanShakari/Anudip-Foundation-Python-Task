# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red

def traverse_reverse_with_index(input_list):
    for index in range(len(input_list)-1, -1, -1):
        print(f"Element: {input_list[index]}, Original Index: {index}")

original_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
traverse_reverse_with_index(original_list)
