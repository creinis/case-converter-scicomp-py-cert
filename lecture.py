# Case Converter Program

# Step 1

# In this project, you are going to learn about list comprehensions in Python by building a program that 
# can take a camelCase or PascalCase formatted string and convert that to a snake_case formatted string.

# List comprehensions in Python are a concise way to construct a list without using loops or the 
# .append() method. Apart from being briefer, list comprehensions often run faster.

# Start defining a new function named convert_to_snake_case() that accepts a string named 
# pascal_or_camel_cased_string as input.

def convert_to_snake_case(pascal_or_camel_cased_string):
    pass

# Step 2

# Now create a new list named snake_cased_char_list inside the function. 
# You can use a set of empty square braces to create the new list.

# This list will hold the characters of the string after you have converted them to snake case.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [] 

# Step 3

# Now that you have an empty list in place, you can start iterating through the input string 
# and start converting each character to snake case.

# Use a for loop to iterate through the pascal_or_camel_cased_string. 
# Make sure to name the target variable char which is short for character.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        pass

# Step 4

# Uppercase characters in camel case or pascal case indicate the start of new words.

# Inside the loop body, use an if statement in conjunction with the .isupper() 
# string method to check for uppercase characters and move pass inside the new if statement.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            pass

# Step 5

# Inside the if statement body, you need to convert any uppercase character to lowercase and prepend 
# an underscore to this lowercase character.

# Use the .lower() string method to convert uppercase characters to lowercase characters. 
# You can then concatenate an underscore to the character using the plus sign.

    #  '_' + char.lower()

#Assign the modified character to a variable named converted_character inside the if statement body.

        if char.isupper():
            converted_character = '_' + char.lower()

# Step 7

# Add an else clause on the same level as the existing if statement, inside the for loop. 
# Add characters that are already in lowercase to the list of converted characters inside the body 
# of the else clause.

        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)



