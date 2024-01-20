# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Pseudocode

# Letting the user input a word
user_input = input("Type a word: ")

# Creating a function for removing letters 
def remove_chars(word, number):   
    print("Original word:", word)
    basis = word[number:]
    result = "New word: " + basis
    
    return result

# Showing and printing the result 
