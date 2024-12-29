# i=0
# while i<5:
#     print("i am while loop\n")
#     i+=1
# n=5
# while n>=0:
#     print(" reverse number\t",n)
#     n-=1
#     e=0
#     while e<20:
#          print("even number\t",e)
#          e+=2
 
# o=1
# while o<20:
#   print("odd number\t",o)
#   o+=2
  
# t=int(input("Enter number for table\t"))
# x=1
# while(x<=10):
#     print(t,"*",x,"=",t*x)
#     x+=1
# arr=[1,2,3,4,5,6,7,8,9,10]
# x=0

# while x<len(arr):
    
#     print("\t",arr[x])
#     x+=1

    
# arr=[]
# s=int(input("enter the size of list\t"))
# z=0
# while z<s:
#   el=int(input("enter iteam of list\t"))
#   arr.append(el)
#   z+=1
  
# print("End of list\n")
# x=0
# n=int(input("Enter the the number you want to find\t"))
# print("''''''''''''''''''''''''''''''''''''''")
# while x<len(arr):
#     if(arr[x]==n):
#      print(arr[x],"number is here at index\t",x) 
#     x+=1
    
# i=1
# while i<=5:
#  print("numbers\t",i)
#  if(i==3):
#   break                    #break terminate loop no other irteration     
#  i+=1

 
# i=0
# while i<=10:
 
#  if(i%2==0):
#   i+=1
#   continue              #countinuous skip when i=3 that irteration and g for next irateration    
  
#  print("odd number:\t",i)  
#  i+=1

# i=0
# while i<=10:
 
#  if(i%2!=0):
#   i+=1
#   continue              #countinuous skip when i=3 that irteration and g for next irateration    
  
#  print("even number:\t",i)  
#  i+=1

# list=[1,2,3,4,5]
# for el in list:
#     print("list iteam\t",el)

#     Name=("mughees","mohsan","usman","Ahmad","Hafiz","Ali")
#     for n in Name:
#         print("From group 4",n)
        
# dic={
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
# }
# for x in dic:
#    print("dictionary key's\t",x)
# else:                      #optionaly use else it execute when loop is complete
#     print("this is your dictionary key values")

# str="Islamia University  oF behwalpur"
# for s in str:
#     if(s=="i"):
#         print(s,"found")
#         break
#     print(s,"this is not i")
# else:                         #else not execute because loop break not complete
#     print("The nane of my university")

    #question
# mylist=[1.4,9,16,25,36,49,64,81,100]
# for n in mylist:
#     print(n)
# mytupal=(1,4,9,16,25,36,49,64,81,100,36)
# idex=0
# for t in mytupal:
#     if(t==36):
#         print(t,"is here at ",idex)
#         break
#     print("list element\t",t)
#     idex+=1

    #range function
    
 
# for el in range(7):  #it start from 0 and increase by 1
#          print(el," number is in range")
 
# seq=range(5)
# for el in seq:  #it start from 0 and increase by 1
#
#          print(el," number is at",seq[el])


# for el in range(2,7):  #it start from 2 and end not include
#          print(el," number is in range")

# for el in range(10,21,2):  #it start from 10 and step size is 2 end not include
#          print(el," number is in range")
# for el in range(0,101,2):  #it start from 0 and step size is 2 end not include
#       print(el,"even number")
# for el in range(1,101,2):  #it start from 1 and step size is 2 end not include
#          print(el,"odd number")         

#pass statment it use when loop have no any work
# for i in range(10):  #loop execute without any work statement
#     pass
        
#question
# n=int(input("Enter number\t"))
# sum=0
# for i in range(n):
#     sum=sum+i
#     print("sum is\t",sum)
# n=int(input("Enter number\t"))
n=int(input("Enter number\t"))
fec=1
i=1

while i<=n:
    fec=fec*i
    i+=1
    
print("fectorial is\t",fec)

    
                
        