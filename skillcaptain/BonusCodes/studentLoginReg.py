import re
class Students :
    def __init__ (self, name, roll, email, password):
        self.name =name 
        self.roll =roll
        self.email = email
        self.password =password
    def databaseOperation(choice, studentDictRoll ,studentDictEmail):
        if choice ==1 :
            print("Enter name, roll , email, password(Seperated by comma)")
            inputArr =input().strip().split(',')
            name= inputArr[0]
            roll =inputArr[1]
            email =inputArr[2]
            password = inputArr[3]
            stat = addUser(name, roll, email, password)
            if stat == 'Success':
                  Student =Students(name, roll, email, password)
                  studentDictEmail[email] =Student
                  studentDictRoll[roll] =Student
                  print("Registration successful")
            else:
                  print("Registration failed")
        if choice ==2 :
              print("Enter Roll/Email and Password (Seperated by comma)")
              inputArr =input().strip().split(',')
              roll_email = inputArr[0]
              password = inputArr[1]



            
def addUser(name, roll, email, password):
        if validateEmail(email) and validateRoll(roll) and validatePassword(password):
            return "Success"
        else:
            return "Failure"
        
def loginService(roll_email, pwd, studentDictRoll, studentDictEmail):
      studentObj = None
      if roll_email in studentDictEmail:
       studentObj=studentDictEmail[roll_email]
      elif roll_email in studentDictRoll :
       studentObj = studentDictRoll[roll_email]
      
      if studentObj and studentObj.password ==pwd:
           return "Success"
      return "Failure"

        

def validateEmail(email):
        pattern = "^[a-z]+[.]?[a-z]*@gmail.com"
        prog =re.compile(pattern)
        return prog.match(email) is not None
def validateRoll(roll):
        roll =str(roll)
        return roll.isdigit()
def validatePassword(password):
        return(len(password)>=8)


if __name__ == "__main__":
     studentDictRoll ={}
     studentDictEmail ={}
     print("Welcome!!!\n To register choose: 1\n To Login choose: 2\nany other key to exit")
     choice = input("lEnter your choice")
