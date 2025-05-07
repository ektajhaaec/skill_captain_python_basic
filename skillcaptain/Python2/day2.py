# Create a class called Person that represents a person, with properties for their name and age. The Person class should of a constructor that takes two parameters: a String for the person's name and an int for their age. The constructor should set the initial values of the name and age properties based on the passed-in values.
# Once you have created the Person class and its constructor, create two Person objects: one representing a person named "Alice" who is 25 years old, and another representing a person named "Bob" who is 30 years old. Print out the name and age properties of each Person object.

class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def persondetails(self):
        print(f"Name :{self.name}")
        print(f"Age:{self.age}")

Person1 = Person ("Gauri",95)
Person1.persondetails()
Person2 = Person ("Wankhade",101)
Person2.persondetails()