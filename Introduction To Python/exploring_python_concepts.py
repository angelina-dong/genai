# TASK 1
# name, age, and height variables for Harry Potter
name = "Harry Potter"
age = 18
height = 5.11

# uses the variables in a print statement
print("Hey there, my name is", name, "! I'm", age, "years old and", height, "feet tall.")


# TASK 2
num1 = 8
num2 = 7

# adds num1 and num2 together
print("the sum of 8 and 7 is", num1 + num2)

# subtracts num2 from num1
print("the difference of 8 and 7 is", num1 - num2)

# multiplies num1 by num2
print("the product of 8 and 7 is", num1 * num2)

# divides num1 by num2
print("the quotient of 8 and 7 is", num1 / num2)


# TASK 3
# prompts user for a number
user_num = float(input("Enter a number: "))

# user_num is greater than 0
if user_num > 0:
    print("This number is positive. Awesome!")

# user_num is less than 0
elif user_num < 0:
    print("This number is negative. Better luck next time!")

# user_num is not > 0 or < 0, so that means user_num == 0
else:
    print("Zero it is. A perfect balance!")