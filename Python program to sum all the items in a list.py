# 1. Write a Python program to sum all the items in a list. 

def sum_list(items):
    total = 0 
    for item in items:
      total += item 
    return total 



items = [1, 2, 3, 4, 5] 
result = sum_list(items)
print(f"The sum of all the items in the list is: {result}")