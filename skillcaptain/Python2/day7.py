# 1. Create a class called "User" that represents a user in the e-commerce system.
# 2. The "User" class should have attributes for the user's name, email, and password.
# 3. Implement a constructor in the "User" class that takes the name, email, and password as parameters and initializes the attributes.
# 4. Implement a method in the "User" class that displays the user's information.
# 5. Create a user registration function that interacts with the user to collect their information and creates a new "User" object.
# 6. The user registration function should validate the email address and ensure that it is unique among registered users.
# 7. Store the registered user information in a user database (can be a list or a file).
# can we call a class in a function ?
# how can we create a list of lists ?

class User :
    def __init__ (self,name, email, password):
        self. name = name
        self.password = password
        self.email = email

    def getUserInfo(self):
        print(self.name)

def userRegistration(name, email, password):
    userlist =[]
    if email is not None:
      User1 =User(name, email, password)
      userlist.append(User1)
      print(userlist[0])

    else:
      print("email is not present")

userRegistration("gauri","gauri@gmail.com","pyaraekta")
