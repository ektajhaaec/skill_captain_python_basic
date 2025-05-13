# Problem Statement 1: Iterate over a file and print each line using next and iter functions

file = open("/home/ekta/skillcaptain/datas/data.txt",'r')
content = file.readlines()
file.close()
content_list =list(content)
iter = iter(content_list)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))