# Problem Statement: Password Strength Checker
# You have been tasked with creating a Python program that checks the strength of a password entered by a user. The program should assess the password based on certain criteria and provide feedback on its strength.

# Requirements:
# 1. Create a function called `check_password_strength` that takes a password string as input.
# 2. Inside the function, define a set of criteria for password strength. This can include factors such as length, presence of uppercase and lowercase letters, numbers, and special characters.
# 3. Implement checks for each criterion using regular expressions. For example, you can use regular expressions to check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
# 4. Assign a score to the password based on the criteria it meets. You can use a scoring system to determine the strength level, such as assigning points for each criterion met.
# 5. Return the password score from the function.
# 6. In the main program, prompt the user to enter a password.
# 7. Call the `check_password_strength` function with the user's password as an argument.
# 8. Based on the password score, provide feedback to the user on the strength of their password. You can display a message such as "Your password is weak," "Your password is medium strength," or "Your password is strong."

# Example:
# Suppose the user enters the password "P@ssw0rd!". The program should assess the password based on criteria such as length, uppercase letters, lowercase letters, digits, and special characters. If the password meets all the criteria, it can be assigned a score of 5.

# The program should display the following message:

#     Password strength: Your password is strong.

# Note: You can define your own criteria and scoring system based on your preferences or requirements.

# Hint: Use regular expressions to check for the presence of specific characters or patterns in the password string.

import re

def check_password_strength(password):
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    special_ch = re.compile(r'[^a-zA-Z0-9]')
    number = re.compile(r'\d')
    point = 0

    if len(password) >=10 :
        point +=1

    match = upper_case.search(password)
    if match :
        point +=1
    match = lower_case.search(password)
    if match:
        point +=1
    match = special_ch.search(password)
    if match:
        point +=1
    match = number.search(password)
    if match:
        point +=1

    if point < 3 :
        print ("Password strength: Your password is weak")
    elif 3 <= point >5 :
        print ("Password strength: Your password is ok okishh")
    else :
        print ("Password strength: Your password is strong")

if __name__ == "__main__" :
    print ("Enter your password")
    password = input()
    check_password_strength(password)
