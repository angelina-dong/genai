import random

# generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# store variables
guess = 0
attempts = 0

# loop through until guess is the number_to_guess
while guess != number_to_guess:

    # bonus task: limits the number of attempts to 10
    if attempts >= 10:
        print("Game over! Better luck next time!")
        break

    # prompt user to guess a number
    guess = int(input("Guess the number (between 1 and 100): "))
    
    # increment attempts by 1
    attempts += 1

    # inform the user about their guess
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it! You guessed it in", attempts, "attempt(s)!")