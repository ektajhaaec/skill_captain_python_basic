#   # Parent class
#     class Animal:
#         def __init__(self, name):
#             self.name = name

#         def speak(self):
#             print(f"{self.name} is making a sound.")

#     # Child class inheriting from Animal
#     class Cat(Animal):
#         def __init__(self, name):
#             super().__init__(name)

#         def speak(self):
#             print(f"{self.name} says Meow!")

#     # Child class inheriting from Animal
#     class Dog(Animal):
#         def __init__(self, name):
#             super().__init__(name)

#         def speak(self):
#             print(f"{self.name} says Woof!")

#     # Creating objects of child classes
#     my_cat = Cat("Whiskers")
#     my_dog = Dog("Buddy")

#     # Calling methods of parent and child classes
#     my_cat.speak()  # Output: Whiskers says Meow!
#     my_dog.speak()  # Output: Buddy says Woof!

# Problem Statement Create a child class named "Truck" that inherits from the Vehicle class. 
# Add an additional attribute "load_capacity" to the Truck class. Implement a method called "display_info()" 
# that prints the brand, model, and load capacity of the truck. Override the "display_info()" method to include the load capacity in the output.

class Vehicle :
    def __init__ (self, brand,model):
        self.brand =brand
        self.model =model

    def display_info(self):
        print(f"{self.brand}{self.model}")

class Truck(Vehicle):
    def __init__ (self,load_capacity,brand ,model):
        self.load_capacity = load_capacity
        super().__init__(brand ,model)

    def display_info(self):
        print(f"{self.brand}{self.model}{self.load_capacity}")

truck1 = Truck("tata","r",100)
truck1.display_info()