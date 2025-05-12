# Task 1
python_amazing_string = "Python is amazing!"

# get characters 0:5
first_six = python_amazing_string[:6]

# get characters a-g in amazing, index 10:one before the last char of the string
amazing = python_amazing_string[10:-1]

# reverse the string
reverse = python_amazing_string[::-1]

print("Original string:", python_amazing_string)
print("First word:", first_six)
print("Amazing part:", amazing)
print("Reversed string", reverse)


# Task 2
print("") # print empty line as separatator between tasks

hello = " hello, python world! "

# use strip() to remove extra spaces
remove_extra_spaces_string = hello.strip()

# use capitalize() to capitalize the first letter
captalize_first_letter_string = remove_extra_spaces_string.capitalize()

# use .replace() to replace 'world' with 'universe'
replace_world_string = captalize_first_letter_string.replace("world", "universe")

# use .upper() to convert the string to uppercase
uppercase_string = replace_world_string.upper()

# print results
print("Remove extra spaces:", remove_extra_spaces_string)
print("Capitalize the first letter:", captalize_first_letter_string)
print("Replace 'world' with 'universe':", replace_world_string)
print("Convert string to uppercase:", uppercase_string)


# Task 3
print("") # print empty line as separatator between tasks

# prompt user for a word
user_input = input("Enter a word: ")

# if string is the same as the revese (case-insensitive), it is a palindrome 
if user_input.lower() == user_input[::-1].lower():
    print("Yes, '" + user_input + "' is a palindrome!")
else:
    print("No, '" + user_input + "' is not a palindrome!")