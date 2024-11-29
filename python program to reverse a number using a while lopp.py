# 1. Write a python program to reverse a number using a while loop. 

# function to reverse a number 
def reversed_num_function(number):
    reversed_num = 0
    while number > 0 :
        digit = number % 10
        reversed_num = reversed_num *  10 + digit
        number = number // 10
    return reversed_num 

# input
number = int(input("Enter a number to reverse: "))

reversed_number = reversed_num_function(number)

# Display the result
print(f"The reversed number is: {reversed_number}")