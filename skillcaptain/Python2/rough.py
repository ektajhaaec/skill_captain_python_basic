class User :
    def __init__ (self,name, email, password):
        self. name = name
        self.password = password
        self.email = email

    def getUserInfo():
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