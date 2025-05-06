# Develop a Python program to perform conversions between a list and a set, adhering to the following requirements:
#  1. Define a list with some elements.
#  2. Design a function that converts the list into a set.
#  3. Design another function that converts a set into a list.
#  4. Print both the converted list and set.
def list_to_set(list1):
    print(list1)
    set1= set(list1)
    print(set1)
    list_updated =list(set1)
    print(list_updated)
    
list1= [1,1,2,4,3,5,6,6,7,85,8,9,5,10]
list_to_set(list1)