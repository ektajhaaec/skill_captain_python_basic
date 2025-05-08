import random
import string


user_input = int(input("Enter the number of names"))
letters = list(string.ascii_lowercase)
file = open("/home/ekta/skillcaptain/datas/python2_day6.txt", 'w' )

vowels =['a','e','i','o','u']
syllables = []
namelist = []
for l in letters :
    for v in vowels:
        syllable = l+v     
        syllables.append(syllable)
for i in range(user_input) :
   name = random.sample(syllables,3)
   namestr= ''.join(name)
   namelist.append(namestr)

set(namelist)
for i in namelist:
    file.write(i+"\n")




   
   





