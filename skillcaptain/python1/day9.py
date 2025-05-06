# my_dict = {'name':'ekta','age':39}
# print(my_dict['age'])
# my_dict['age'] =99
# print(my_dict['age'])
# my_dict['occupation'] ='Engineer'
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# Compose a Python program to execute various operations on a given dictionary:
#  1. Insert a new key-value pair into the dictionary.  2. Delete a designated key-value pair from the dictionary.  
# 3. Modify the value associated with a specified key in the dictionary.  4. Verify the existence of a key in the dictionary. 
#   5. Display all the keys present in the dictionary.

alpha_num_dict = dict(a= 10,b= 20, c= 30, d= 40, e= 50)
print(alpha_num_dict.items())
alpha_num_dict['f'] = 60
print(alpha_num_dict.items())
del alpha_num_dict['a']
print(alpha_num_dict.items())
alpha_num_dict['b'] = 60
print(alpha_num_dict.items())
print(alpha_num_dict['b'])
print(alpha_num_dict.keys())
