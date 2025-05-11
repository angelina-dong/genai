# TASK 1
# prompt user for starting number
starting_number = int(input("Enter a starting number to count down from: "))

# loop until number hits 0
while starting_number > 0:

    # print the number, add a space between each one
    print(starting_number, end=" ")

    # decrement starting number by 1
    starting_number -=1

print("Blast off! 🚀")


# TASK 2
print("") # print empty line as separatator between tasks

# prompt user to enter a number to generate its multiplication table for that number (from 1 to 10)
multiplication_table_number = int(input("Enter a number to generate its multiplication table: "))

# loop from 1 to 10
for i in range(1, 11):

    # print equation and product, separating each equation with a space
    print(multiplication_table_number, "x", i, "=", multiplication_table_number * i, end=" ")

# TASK 3
print("") # print as separatator between tasks
print("") # print empty line as separatator between tasks

# prompts users to enter a number used to calculate its factorial
factorial_number = int(input("Enter a number to calculate the factorial: "))

# varaible to store the factorial value
factorial = 1

# iterate backward from the factorial number to 0, decrementing by 1 each time
for i in range(factorial_number, 0, -1):
    
    # multiply current factorial value by i
    factorial *= i

# print the factorial_number's factorial
print("The factorial of", factorial_number, "is", factorial)