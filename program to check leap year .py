# 1. Python program to check leap year 

# function to check if a year is as leap year
def is_leap_year(year):
    if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# input year from the user
year = int(input("Enter a year: "))

# check if the year is a leap year
if is_leap_year(year):
    print(f"{year} us a leap year.")
else:
    print(f"{year} is not a leap year.")
