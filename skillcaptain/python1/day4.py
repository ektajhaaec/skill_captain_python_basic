# Implement a Python function that define a person's age and generates distinct messages based on predefined conditions:
# If the age is less than 18, the function should return "You are a minor.
# If the age is between 18 and 65 (inclusive), the function should return "You are an adult.
# If the age is greater than 65, the function should return "You are a senior citizen.

# Output:
# You are a minor.
# You are an adult.
# You are a senior citizen.

# Explanation:
# For age 15, 35 and 70.

def calculating_age (age):
    if age <18:
        print("You are a minor.")
    elif 18 <= age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

age =76
calculating_age(age)