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

    
print("Welcome to the Recursive Artistry Program!")

# continues asking for user input until the user exits
while True:

    # tracks whether the user entered number is valid/corresponds to an option
    is_valid = False

    # continues asking for new user input until the number is valid
    while not is_valid:
        try:
            # prompts user to enter a number
            user_num = int(input("Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Exit > "))

            # checks if user_num is 1, 2, or 3
            if user_num in [1, 2, 3]:
                is_valid = True
            
            # if user_num is not 1, 2, or 3, it is not a valid choice
            else:
                print("Invalid choice! Please enter a number 1-3.")
        
        # handles if user input is not an integer
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # ensures that user_num is an integer 1, 2, or 3
    if is_valid:

        # if user_num is 1, call factorial
        if user_num == 1:
            number = int(input("Enter a number to find its factorial: "))
            print(f"The factorial of {number} is {factorial(number)}.")

        # if user_num is 2, call fibonacci
        elif user_num == 2:
            fib_pos = int(input("Enter the position of the Fibonacci number: "))
            print(f"The {fib_pos}th Fibonacci number is {fibonacci(fib_pos)}.")
        
        # if user_num is 3, exit the loop
        elif user_num == 3:
            break
    
print("Thank you for running the Recursive Artisiry Program!")