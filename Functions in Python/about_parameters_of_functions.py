# TASK 1
# accepts a name as a parameter and prints a personalized greeting
def greet_user(name):
    print(f"Hello {name}! Welcome aboard.")

# takes two numbers as parameters and adds them together to get their sum
def add_numbers(num1, num2):
    sum = num1 + num2 
    print(f"The sum of {num1} and {num2} is {sum}.")
    return sum

# call the functions
greet_user("Alice")
add_numbers(5, 10)


# TASK 2
print("") # print empty line as separatator between tasks

# accepts pet name and animal type, with a default animal type of 'dog'
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# call the function
describe_pet("Buddy")
describe_pet("Whiskers", "cat")


# TASK 3
print("") # print empty line as separatator between tasks

# acceptsa variable number of arguments for sandwich ingredients
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# call the function
make_sandwich("Lettuce", "Toamto", "Cheese")

# TASK 4
print("") # print empty line as separatator between tasks

# recursive function to calculate the factorial of a number
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
    
# recursive function to calculate the nth number in the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# call the functions
fact = 5
fib = 6
print(f"Factorial of {fact} is {factorial(fact)}. The {fib}th Fibonacci number is {fibonacci(fib)}.")