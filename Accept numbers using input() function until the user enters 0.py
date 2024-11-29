#  4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

 # Function to sum numbers until user enters 0
def sum_numbers():
    total = 0
    while True:
        number = float(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        total += number
    return total

# Calculate the sum of all numbers
total_sum = ()

# Display the result
print(f"The sum of all entered numbers is: {total_sum}")
