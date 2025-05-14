import logging

# set up errors to log to error_log.txt for the bonus step
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

print("Welcome to the Error-Free Calculator!")

# continue until user chooses to exit
while True:

    # continue prompting user for operation until their input is valid
    while True:
        try:
            operation = int(input("Choose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit > "))
            
            # check to ensure the int is 1, 2, 3, 4, or 5
            if operation not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please type a number 1-5.")
            else:
                break
        
        # catch non int values and log the error
        except ValueError as e:
            print("Invalid input. Please enter a number 1-5")
            logging.error(f"ValueError occured: {e}")
    
    # check if user wishes to exit the program, and if so, exit
    if operation == 5:
        print("Goodbye!")
        break
    
    # prompt user for two numbers until their inputs are valid
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break

        # catch non float values and log the error
        except ValueError as e:
            print("Invalid input. Please try again and ensure you are entering numerical values.")
            logging.error(f"ValueError occured: {e}")

    try:
        # user chose addition, add the numbers together
        if operation == 1:
            result = num1 + num2

        # user chose subtraction, subtract num2 from num1
        elif operation == 2:
            result = num1 - num2

        # user chose multiplication, multiply the numbers together
        elif operation == 3:
            result = num1 * num2

        # user chose division, divide num1 by num2
        elif operation == 4:
            result = num1 / num2
    
    # catch ZeroDivisionError and log it if the program attempts to divide by 0
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occured: {e}")
    
    # if no errors are caught, print out the result
    else:
        print(f"Result: {result}")

    # at the end of each operation, error or not, print a statement before the loop loops again
    finally:
        print("Let's calculate something else!")