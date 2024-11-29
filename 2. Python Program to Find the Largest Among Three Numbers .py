# 2. Python Program to Find the Largest Among Three Numbers 

# function to find the largest among three numbers
def find_largest(num1, num2, num3): 
    if num1 >= num2 and num1 >= num3: 
        return num1 
    elif num2 >= num1 and num2 >= num3: 
        return num2 
    else: 
        return num3


# input three number form user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))


largest = find_largest(number1,number2,number3)

# Display the result 
print(f"The largest number among {number1}, {number2}, and {number3} is: {largest}")