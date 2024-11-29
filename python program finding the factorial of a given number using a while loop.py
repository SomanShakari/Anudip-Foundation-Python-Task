# 3. Write a python program finding the factorial of a given number using a while loop.


# function to find the factorial of the umber
def factorial(number):
    result = 1
    while number >1:
        result *= number
        number-=1
    return result

# input
number = int(input("Enter a number to find its factorial: "))

if number <0:
    print("Factorial is not defined for negative numbers. ")
else:
    fact = factorial(number)

    print(f"The factorial of {number} is: {fact}")