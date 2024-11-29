# 3. Python Program to Check if a Number is Positive, Negative or 0 

# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Input number from the user
number = float(input("Enter a number: "))

# Check the number and get the result
result = check_number(number)

# Display the result
print(f"The number {number} is {result}.")
