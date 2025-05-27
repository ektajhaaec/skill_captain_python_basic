# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# class Node :
#     def __init__(self,data):
#         self.data =data
#         self.next =None

# class LinkedList:
#     def __init__(self):
#         self.head =None
#     def insert(self,data):
#         new_node =Node(data)
#         if not self.head:
#             self.head =new_node
#             return
#         last =self.head
#         while last.next:
#             last = last.next
#         last.next =new_node
#     def print_list(self):
#         current =self.head
#         while current:
#             print(current.data, end ="->")
#             current =current.next
#         print("None")

# linkedList = LinkedList()
# linkedList.insert(10)
# linkedList.insert(20)
# linkedList.print_list()

def linked_list(self ,data =0, next =None):
    self.data =data
    self.next =next


def merge_sorted_list(self,l1 ,l2):
    l3 =linked_list()
    pointer = l3

    while l1 is not None and l2 is not None :
        if l1.data <l2.data:
            pointer.next =l1
            l1=l1.next
        else:
            pointer.next =l2
            l2 =l2.next
            pointer =pointer.next
    return l3.next

l1 =[1,2,3]
l2 = [4,2,4]
print(merge_sorted_list(l1 , l2))



    
