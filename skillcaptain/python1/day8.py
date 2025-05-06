def concatinate_list(list1,list2):
   
    for i in list2:
       list1.append(i)
    return list1

list1 = [1,2,3]
list2 = ["a", "b", "c"]
print(concatinate_list(list1,list2))
