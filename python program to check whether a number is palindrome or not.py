# 2. Write a python program to check whether a number is palindrome or not? 

# function to check if a number is palindrome or not
def is_palindrome(number):
    num_str = str(number)

    reversed_str  = num_str[::-1]

    return num_str == reversed_str


# input numbers from the user
number = int(input("Enter a number to check if it is a palindrome: "))

if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not palindrome")