# 2. Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"

# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Function to remove newlines from a string
def remove_newlines(s):
    return s.replace("\n", " ")

# Remove newlines from the string
cleaned_string = remove_newlines(string)

# Display the result
print("Original String:")
print(string)
print("\nString after removing newlines:")
print(cleaned_string)
