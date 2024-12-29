##Lecture 1
# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# print("the sum is\t",n1+n2)

# r=int(input("Enter the length of sides of seqqure\t"))
# print("the area of sequre\t",r*r)

# n1=float(input("Enter the first flaot number"))
# n2=float(input("Enter the second  flaot number"))
# print("the sum is\t",(n1+n2)/2)

# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# print(n1>=n2)


##Lecture 2
# name=input("Enter your name\t")
# print("size of your name is \t",len(name))

# name=input("Enter your String\t")
# ch=input("Enter the char which you want to count\t")
# print(" accourance of",ch,"in your string is ",name.count(ch))




# n=int(input("Enter the  number"))
# if(n%2==0):
#     print("even number")
# else:
#     print("odd number")    

# a=int(input("Enter the first  number\t"))
# b=int(input("Enter the second  number\t"))
# c=int(input("Enter the third  number\t"))
# d=int(input("Enter the fourth  number\t"))

# if(a>b):
#     if(a>c):
#         if(a>d):
#               print(a,"is greater number")
#         else:
#             print(d,"is greater number")
#     else:
#         if(c>d):
#             print(c,"is greater number")
#         else:
#             print(d,"is greater number")    
            

# else:
#     if(b>c):
#         if(b>d):
#          print(b,"is gdreater number")
         
#         else:
#          print(d,"is greater number")    
#     else:
#         if(c>d):
#             print(c,"is greater number") 
#         else:
#             print(d,"is greater number")            
# num=int(input("Enter the number\t"))
# if(num%7==0):
#     print(num,"is multiple of 7 number")
# else:
#     print(num,"is not multiple of 7 number")


##lecture 3
# moive_list=[]
# m1=input("Enter your 1st favirout moive\t")
# m2=input("Enter your 2nd favirout moive\t")
# m3=input("Enter your 3rd favirout moive\t")
# moive_list.append(m1)
# moive_list.append(m2)
# moive_list.append(m3)
# print("your movies list is\t",moive_list)

# pl=list(input("Enter your list\t"))
# pl2=pl.copy()
# pl2.reverse()
# if(pl==pl2):
#     print("it is palidrom",pl==pl2)
# else:
#       print("it is not palidrom",pl==pl2)   
# 

# t=("C","D","A","A","B","B","A")
# print("number of student have grade A is\t",t.count("A"))

# marks=int(input("Enter your marks\t"))
# if(marks<=90 and marks>80):
#     print("your grade is A")
# elif(marks<=80 and marks>70):
#     print("your grade is B")
# elif(marks<=80 and marks>60):
#     print("your grade is C")
# elif(marks<=60 and marks>50):
#     print("your grade is D")
# else:
#     print("inviled input")

##lecture 4

# student={}
# s1=input("Enter your first subject\t")
# n1=int(input("Enter marks of  first subject\t" ))
# s2=input("Enter your second subject\t")
# n2=int(input("Enter marks of  second subject\t" ))
# s3=input("Enter your third subject\t")
# n3=int(input("Enter marks of  third subject\t" ))
# student.update({s1:n1})
# student.update({s2:n2})
# student.update({s3:n3})
# print("your dictionary\t",student)

# set={9,9.0}     #save same value in set with help of string
# print(set)

# set1={9,"9.0"}     #save same value in set with help of string
# print(set1)
# set2={("int",9),("float",9.0)} #save same value in set with help of bulit in data type
# print(set2)

##lecture 5
# n=1
# while n<=100:
#     print(n)
#     n+=1

# n=100
# while n>=1:
#     print(n)
#     n-=1

# n=int(input("Enter number for table"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# list=[1,4,9,16,25,36,49,64,81,100]
# n=0
# while n<len(list):
#     print(list[n])
#     n+=1

# list=(1,4,9,16,25,36,49,64,81,100,81)
# num=81
# n=0
# while n<len(list):
#     if(list[n]==num):
#      print(num,"is found at",n)
#     n+=1

# list=[1,4,9,16,25,36,49,64,81,100]

# for i in list:
#     print(i)


# list=(1,4,9,16,25,36,49,64,81,4,100)
# x=4
# indx =0
# for i in list:
#     if(x==i):
#      print(x, "is at",indx)
#     indx+=1

# for i in range(1,101):     #last index not include
#     print(i)
# for i in range(100,0,-1):
#     print(i)    

# n=int(input("enter number for table\t"))
# for i in range(11):
#     print(n,"*",i,"=",n*i)

# for i in range(5):
#     pass                  #null statment
# print("end loop")

# i=1
# sum=0
# while i<=16:
#   sum+=i
 
#   i+=1
# print("sum of first 15 number",sum)  
# fac=1
# for i in range(1,6):
#   fac*=i
# print("factorial of first five number",fac)  

##lecture 6
# def p_length(list):
#     print(len(list))

# list=["a","b",1,4,7]
# p_length(list)    

# def p_list(list):
#     for  i in list:
#         print(i,end=",")

# list=["Ali","Usman","Ahmad"]
# p_list(list)        


# def fact(n):
#     fact =1
#     for i in range(1,n+1):
#         fact*=i
     
#     print(fact)

# num=int(input("Enter number for factorialt\t"))    
# fact(num)


# def USA_to_pk(doll):
#     doll*=280
#     print("pakistani ruppes\t",doll)
# d=int(input("Enter US doller\t")) 
# USA_to_pk(d)  
# def check_number(num):
#     if(num%2==0):
#         return "even"
#     else:
#         return"odd"
# n=int(input("Enter number\t"))
# print(check_number(n))  


# def sequence(n):
#     if(n==0):
#         return
#     print(n)
#     sequence(n-1)

# sequence(5)

# def sum(n):
#     if(n==0):
#       return 0
    
#     return sum(n-1)+n   

# n=int(input("Enter a number for sum\t "))
# print(sum(n))


# def fact(n):
#     if(n==0 or n==1):
#         return 1 
#     f=fact(n-1)*n
#     return  f
# n=int(input("Enter a number for factorial\t"))
# print(fact(n))

# def el_list(list,indx):
    
#     if(indx==len(list)):
#         return
#     print(list[indx])
#     el_list(list,indx+1)

# list=[1,2,3,4,"a","b"]
# el_list(list,0)
    
