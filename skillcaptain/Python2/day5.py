#Problem Statement:Write a Python program that reads a text file called "data.txt" and counts the number of lines in the file.

file = open ("/home/ekta/skillcaptain/datas/data.txt","r")
content= file.readlines()
file.close()
print(len(content))

