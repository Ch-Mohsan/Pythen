# list=[1,2,3,4,5]
# print(list)
# print("data type of list\t",type(list))
# print("value at index 2 is\t",list[2])
# print("value at index 4 is\t",list[4])
# print("length of list is\t",len(list))
# # python allow us to store data of different type in same list
# student=["mohsan",123,5.7]
# print("student list is\t",student)
# #list is muteable means we can change insert,remove,updste
# student[0]="Ali"
# #list silcing
# marks=[50,45,60,65,75,70]
# print("element of marks list index 0 to 3\t",marks[0:3]) #last index not include
# print("element of marks list without start index to 3\t",marks[:3]) #auto access starting index
# print("element of marks without giving last index from 0 1\t",marks[1:]) #auto access last index

# #nagative indexing
# print("element of marks list index -1 to -3\t",marks[-3:-1]) #last index not include

#                           #list function makes changes in original list
# num=[5,3,2,1,4,6,7]
# print("orignal list is\t",num)
# num.append(4)
# print("list after appond 4\t",num)
# num.sort()     #accessding order sorting
# print("list after  accessending sorting sort\t",num)
# num.sort(reverse=True)     #accessding order sorting
# print("list after  decending order sorting\t",num)

# num.reverse()
# print(" list after reverse\t",num)
# num.insert(1,8)
# print("list after insert 8 at index 1 sort\t",num)
# num.remove(1)
# print("list after remove first occance of number\t",num)
# num.pop(3)
# print("list after pop the value from index 3\t",num)


#                     #string sorting
# str=["B","A","C","D","F","E"]
# str.sort()      #sorting
# print("list after   sorting sort\t",str)

# str.insert(1,"Z")
# print("list after insert Z at index 1 sort\t",str)

#                                     #  question
# list=[]
# m1=input("Enter first song")
# m2=input("Enter second song")
# m3=input("Enter third song")
# list.append(m1)
# list.append(m2)
# list.append(m3)
# print("list of your favirout songs is:\t",list)
#                #create a palidrom list which means same after reverse
# l1=input("Enter the first element of list\t")
# l2=input("Enter the second element of list\t")
# l3=input("Enter the third element of list\t")
# l4=input("Enter the fourth element of list\t")
# list1=[l1,l2,l3,l4]
# list2=list1.copy()
# list2.reverse()
# if(list1==list2):
#     print("it is palindrom")
# else:
#     print("it is not palidrom")
