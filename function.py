def hell():
  print("Hellow pythen function")  
def sum(a,b):
    return a+b
def subtact(a,b):
    return a-b
def multiy(a,b):
    return a*b
def power(a,b):
    return a**b
def division(a,b):
    return a/b
def mud(a,b):
    return a%b
hell()

# n=int(input("Enter 1st number\t"))
# m=int(input("Enter 2nd number\t"))
# print("sum function\t",sum(n,m))
# print("subtaction function\t",subtact(n,m))
# print("multiplay function\t",multiy(n,m))
# print("division function\t",division(n,m))
# print("modulas function\t",mud(m,m))
# print("power function\t",power(n,m))
# def sum1(a,b,c):
#     return a+b+c

# def avarge(a,b,c):
#     return a+b+c/3
# n1=int(input("Enter 1st number\t"))
# n2=int(input("Enter 2nd number\t"))
# n3=int(input("Enter 3rd number\t"))
# print("avarge of 3number is\t",avarge(n1,n2,n3))
# print("Sum of number is\t",sum1(n1,n2,n3))
# def num(a=6,b=6):     #defult parameters 
#     return a==b
# print("equaity of numbers\t",num())
#question
# city=["multan","karach","okhara","Bwp"]
# def len(a):
#     num=0
#     for c in a:
#         num+=1
#     print("length of list\t",num)

# len(city)
  
# def line(a):
#     for i in a:
#      print(i, end=" ")
 
# line(city)   
# def factorial(n):
#     f=1  
#     for i in range(1,n+1):
#         f=f*i
#     print("fectorial is\t",f) 

# num=int(input("enter number for fectorial\t"))        
# factorial(num)       

# def coventer(r):
#     val=0
#     val=r*250
#     print("Pakistani rupees\t",val)
    
# rep=int(input("enter USA $ :\t"))
# coventer(rep)
# def Pk_coventer(r):
#     val=0
#     val=r/250
#     print("USA \t",val,"$")
    
# rep=int(input("pakistani rupees :\t"))
# Pk_coventer(rep)
def even_odd(a):
    if(a%2==0):
        return "even"
        
    else:
        return "odd"
eo=int(input("enter number\t"))
str=even_odd(eo)
print("even or odd\t",str)      