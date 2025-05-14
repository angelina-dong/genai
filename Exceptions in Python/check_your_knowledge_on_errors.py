# Task 1
while True:
    try:
        # prompt user to enter a number
        num = float(input("Enter a number: "))
        # attempt to divide 100 by the user's number
        divided_by_100 = 100 / num
        print(f"100 divided by {num} is {divided_by_100}")
        break

    # handle when the user enters non-numeric input
    except ValueError:
        print("Invalid input! Please enter a valid number.")

    # handle when attempting to divide by zero
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")

    
# Task 2
print("") # print empty line as separatator between tasks

# create a list and dictionary
fruit = ["apple", "banana"]
inventory = {"apple": 3, "banana": 5}

# attempt to access an index out of range and catch the IndexError in an exception caused by this
try:
    print(fruit[2])
except IndexError:
    print("IndexError occured! List index out of range.")

# attempt to access a key in the dictionary that doesn't exist and catch the KeyError in an exception caused by this
try:
    print(inventory["mango"])
except KeyError:
    print("KeyError occured! Key not found in the dictionary.")

# attempt to apply the '+' operation to a string and an int (inappropriate types) and catch the TypeError in an exception caused by this
try:
    sum = "one" + 2
except TypeError:
    print("TypeError occured! Unsupported operand types.")


# Task 3
print("") # print empty line as separatator between tasks

try:
    # prompts user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # attempts to divide the first number by the second number
    result = num1 / num2

# handles non float input values
except ValueError:
    print("Invalid input! Cannot complete division with non-numerical values.")

# catches attempts to divide by zero
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")

# if no exceptions occur, display the result
else:
    print(f"The result is {result}.")

# print a closing message regardless of exceptions
finally:
    print("This block always executes.")
    
