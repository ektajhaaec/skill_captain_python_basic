# Write a program using a while loop to print all the numbers from 1 to 10. Create a list of names. Use a for loop to iterate over the list and print a personalized greeting for each name.

# Output:
# 1 2 3 4 5 6 7 8 9 10
# Hello, Alice! Hello, Bob! Hello, Charlie! Hello, David! Hello, Eve!

# Explanation:
# This program utilizes a while loop to print numbers from 1 to 10 horizontally, separated by spaces. It then uses a for loop to print personalized greetings for each name horizontally, with each greeting separated by spaces.


def numberfunc(num):
    start =1
    while start <=num:
        print(start)
        start += 1

def namefunc (name_list):
    for i in name_list:
        print(f"Hello, {i}!")
numberfunc(10)
name_list =["ekta","bob"]
namefunc(name_list)