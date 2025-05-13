# Requirements: Create a decorator called authorize that checks if a user is authorized to access a function. 
# The decorator should take a username as an argument and compare it with a list of authorized users. 
# If the user is authorized, the function should be executed. 
# Otherwise, it should print an error message.
def authorize(func):
    def wrapper(user_name):
        name_list =["ekta" ,"sagar" ,"billu" ,"puchka"]
        if user_name in name_list:
            func(user_name)
        else:
            print("user is not authorized")
    return wrapper

@authorize
def welcome(user_name):
    
    print(f"Welcome to the homepage{user_name}")

        
user_name = input ("Enter a user name")

welcome(user_name)

