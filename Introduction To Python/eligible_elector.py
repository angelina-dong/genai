# prompts user for age
age = int(input("How old are you? "))

# checks if age is 18 or above
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
# age is not 18 or above, so age is less than 18
else:
    print("Oops! You’re not eligible yet. But hey, only", 18 - age, "more year(s) to go!")

print("Thank you for using Eligible Elector 😊!")