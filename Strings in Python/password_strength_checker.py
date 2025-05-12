# prompt user to input a password
password = input("Enter a password: ")

# stores valid special characters, in this case, valid special characters include @, #, and $
special_chars = "@#$"

# checks if password is at least 8 characters
at_least_8_chars = len(password) >= 8

# checks if password contains at least one uppercase letter
contains_upper = any(c.isupper() for c in password)

# checks if password contains at least one lowercase letter
contains_lower = any(c.islower() for c in password)

# checks if password contains at least one digit
contains_digit = any(c.isdigit() for c in password)

# checks if password contains at least one special character
contains_special = any(c in special_chars for c in password)

# variable to keep track of password strength (for bonus challenge)
# for any requirement missing, subtract 2 from the score
score = 10

# keeps track of the requirements' messages that the password does NOT meet
password_does_not_meet_msgs = []

if not at_least_8_chars:
    password_does_not_meet_msgs.append("at least 8 characters")
    score -= 2
if not contains_upper:
    password_does_not_meet_msgs.append("one uppercase letter")
    score -= 2
if not contains_lower:
    password_does_not_meet_msgs.append("one lowercase letter")
    score -= 2
if not contains_digit:
    password_does_not_meet_msgs.append("one digit")
    score -= 2
if not contains_special:
    password_does_not_meet_msgs.append("one special character (@, #, $)")
    score -= 2

# if no messages are added to password_does_not_meet_msgs, then the password is strong
if not password_does_not_meet_msgs:
    print("Your password is strong! 💪")

# if there is at least one msg in password_does_not_meet_msgs, then print msg informing what the password needs
else:
    print("Your password needs " + " and ".join(password_does_not_meet_msgs) + ".")

# print the password's strength
print("Password Strength: " + str(score) + "/10.")