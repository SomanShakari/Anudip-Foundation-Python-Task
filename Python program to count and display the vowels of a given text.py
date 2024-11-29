#  4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”
# Function to count and display vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    vowels_found = []

    for char in s:
        if char in vowels:
            count += 1
            vowels_found.append(char)
    
    return count, vowels_found

# Input string from the user
string = input("Enter a string: ")

# Count and display the vowels
vowel_count, vowels_found = count_vowels(string)

# Display the result
print(f"Total number of vowels: {vowel_count}")
print("Vowels found:", ' '.join(vowels_found))
