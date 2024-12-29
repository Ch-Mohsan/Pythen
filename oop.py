# class Student:    #class
           
#      name="mohsan"
        
# s1=Student()    #s1 is object
# print(s1.name)        
# s2=Student()    #s2 is object
# print(s2.name)  

##contructor
# class D:
#     def __init__(self):
#         print(self)       #self parameter point out the object of class   
#         print("i am the defult constractor of class") 

# s1=D()  # contractor call automatcally when create object     

#parameterized constructor
# class P:
#      def __init__(self,name):
#          print("print your name")
#          self.name=name
 
# p1=P("im am p1")
# print(p1.name)    
# p2=P("im am p2")
# print(p2.name)

#Attritutes veriable
#object attributes different of every object create with self 
#class attributes same for whole class

# class College:
#  coll_name="Superior"         #class attributes
#  name="anyone"  
#  def __init__(self,name,age):
#   self.name=name        #object attributes
#   self.age=age

# c1=College("Ali",19)
# print("name of your  college is ",c1.coll_name)   #access class veriable with object
# print("your 1st student is",c1.name)  #here same name of object and class veriable but here access only objec veriable name  
# print("His age is",c1.age)
# c2=College("Ahmad",20)
# print("name of your college is ",College.coll_name)  #access cl;ass veriable with class name
# print("your 2nd student is",c2.name)
# print("His age is",c2.age)


# class Arithmatic:
#     action="this is your Result"
#     def __init__(self,op):
#         self.op=op

#     def calculation(self,a,b): #every method must have  defult self parameter
#         if(self.op=="+"):
#             return a+b
#         elif(self.op=="-"):
#             return a-b
#         elif(self.op=="*"):
#             return a*b
#         elif(self.op=="/"):
#             return a/b
#         elif(self.op=="%"):
#             return a%b
#         elif(self.op=="**"):
#             return a**b
#         else:
#             print("inviled operator")
#             return

# n1=int(input("Enter first number\t"))
# n2=int(input("Enter first number\t"))
# p=input("Enter arithmitic operator \t")
# a=Arithmatic(p)
# print(a.action)
# print(a.calculation(n1,n2))


##static function which not have defult self parameter
# class Python:                  
#     @staticmethod      #it is decorator this makes a function static
#     def p_hellow():     #it is class level method
#         print("Hellow pythen world!")

# # py=Python()
# # py.p_hellow()    
# Python.p_hellow #it can access with class dont need of object
         
        
#Abstraction 
#heiding un naccessary implimantation and show only important featuear

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.brk=True
#         self.clutch=True
#         print("Car stated!")    
        
# ca=Car()
# ca.start()   

#Encapsulation
#Warping data and function in a single unit(object) it means make a class 


##bank Account
class Bank:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc 
    def get_balance(self):
        return self.bal         

    def Debit_acc(self,amount):
        self.bal-= amount
        print("this is your remation blance",self.get_balance())
    def cridit_acc(self,amount):
        self.bal+= amount
        print("this is your remaing blance",self.get_balance())

    

num1=int(input("Enter your account No "))
amount=int(input("Enter your account balance!\t"))
b1=Bank(amount,num1)
ch=int(input("Enter 1 for Debit\nEnter 2 for Crited\t"))
if(ch==1):
    D_amount=int(input("Enter your ammount for Didt!\t"))
    b1.Debit_acc(D_amount)
if(ch==2):
    C_amount=int(input("Enter your ammount for Cridit!\t"))
    b1.cridit_acc(C_amount)
else:
   print("Inviled choise")
