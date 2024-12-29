# class Del:
#     def __init__(self,name):
#        self.name=name

# d1=Del("Ali")
# del(d1)
##print(d1.name)     here is error because d1 object is delete       

# # ##public attributes

# class Public:
#     def __init__(self,name):
#         self.name=name

# p1=Public("Ahmad")  
# print(p1.name)    #name can access outside the class it is public

# # #private attributes

# class Private:
#     def __init__(self,name):    
#         self.__name=name     #make name veriabel private by __
#     def __password(self,pas):
         
#         print(pas)    

#     def print_data(self):
#         print(self.__name)    #name veriable can use inside the class
#         self.__password("12345")    #password method can use inside the class
   
   
# p1=Private("Ahram")  
#print(p1.name)    #name can not be access outside the class it is private
# p1.print_data()
##p1.__password("123123")        #here is error password methed is private:

#class method
# class Person:
#    name="anyone"
#    def change_name(self,name):
#       ##Person.name=name      #it can  change anyone to new name
#       self.__class__.name=name  #it is another way ta change class veriable
#       print(self.name)
  
#    @classmethod       #use to create class method
#    def change_name1(cls,name):  #access and change class veriable
#       cls.name=name    

   
#p1=Person()
# p1.change_name1("Mugees") #now  change anyone to mugees
# print(Person.name)

# #property method
# class Student:
#     def __init__(self,phy,cs,math):
#         self.phy=phy
#         self.cs=cs
#         self.math=math
#        ## self.avarge=self.phy+self.cs+self.math/3
#     def print_avarge(self):
#         ##self.avarge=str(self.phy+self.cs+self.math/3)
#         print(self.avarge) #change avarge by mehod
 
#     @property    #it can automatically change veriable for latest value
#     def avarge(self):
#          return self.phy+self.cs+self.math/3
        

# s1=Student(91,72,83)
# print(s1.avarge) 
# s1.phy=81
# print(s1.phy)     #marks is changed but avarge is not change
# print(s1.avarge)
# # s1.print_avarge()


##inheritance
#in it chiled class inherited the method and properities of periend class
#multiy level inheritance

# class Grand_father:
#     def __init__(self,):
#       self.__name="Akbar Ali"
#       self.__age=80
#       self.__password=1234
#     def __Account(self):
#         print("Grand_father account in 'HBL' ")
#         print("password of account is\t",self.__password)
#     def Grandfather_info(self):
#         print("Name of grand_father is\t",self.__name)  
#         print("Age of grand_father is\t",self.__age) 
#         self.__Account() 


# class Father(Grand_father):
#     def __init__(self,):
#      super().__init__()     #it is use to access and change prient class attributes   
#      self.__name="Zafar Ali"
#      self.__age=55
#      self.__password=1288
#     def __Account(self):
#         print("Father account in 'UBL' ")
#         print("password of account is\t",self.__password)
#     def father_info(self):
#         print("Name of Father is\t",self.__name)  
#         print("Age of Father is\t",self.__age) 
#         self.__Account() 

# class Chiled(Father):
#     def __init__(self,):
#      super().__init__()        #it is use to access and change prient class attributes
#      self.__name="Mohsan Ali"
#      self.__age=20
#      self.__password=000
#     def __Account(self):
#         print(" account in 'National' Bank ")
#         print("password of account is\t",self.__password)
#     def chiled_info(self):
#         print("Name of chiled is\t",self.__name)  
#         print("Age of chiled is\t",self.__age) 
#         self.__Account() 

# data=Chiled()
# data.Grandfather_info()
# data.father_info()
# data.chiled_info()



#multiple inheritance

# class A:
#     def __init__(self):
#         self.__colour="blue"
#     def wellcomC(self):
#         print("hi",self.__colour,"i am in cass A")  

# class B:
#       def __init__(self):
#         self.__colour="pink"
#       def wellcomB(self):
#         print("hi",self.__colour,"i am in cass B")    
  
# class C(A,B):
#     def __init__(self):
#      A.__init__(self)
#      B.__init__(self)    
#      self.__colour="white"
#     def wellcomA(self):
#         print("hi",self.__colour,"i am in cass C")    
        
# c1=C()
# c1.wellcomA()
# c1.wellcomC()
# c1.wellcomB()



#poylmorphism

##method overloading it means same method in one class

# class Example:
#     def display(self, a=None, b=None, c=None):
#         if a is not None and b is not None and c is not None:
#             print(f"Two arguments: a = {a}, b = {b},c={c}")
#         elif a is not None and b is None:
#             print(f"One argument: a = {a}")
#         elif a is not None and b is not None:
#             print(f"two argument: a = {a}, b={b}")
            
#         else:
#             print("No arguments")

# example = Example()
# example.display()   
# example.display(1) 
# example.display(1, 2)
# example.display(1, 2, 3)

##method overised it means same method in different classes

# class Parent:
#     def display(self):
#         print("This is the display method in the Parent class")

# class Child(Parent):
#     def display(self):
#         print("This is the display method in the Child class")

# parent = Parent()
# child = Child()

# child.display()
# child.display()


##opertor over loading 
# print(1+2)  #sum
# print("mohsan"+"Ali") #concatination
# print([1,2,3]+[4,5,6]) #merge

# ##create complex number
# class Complex:
#     def __init__(self,real,img):
#      self.real=real
#      self.img=img
#     def shownumber(self):
#        print(self.real,"i +",self.img,"j")
#     def add(self,num2):
#        newR=self.real+num2.real
#        newI=self.img+num2.img
#        return Complex(newR,newI)
#     def __add__(self,num2):    #change add function to dunder function
#        newR=self.real+num2.real
#        newI=self.img+num2.img
#        return Complex(newR,newI)
#     def __sub__(self,num2):    #change sub function to dunder function
#        newR=self.real+num2.real
#        newI=self.img-num2.img
#        return Complex(newR,newI)


# c1=Complex(2,3)
# c1.shownumber() 
# c2=Complex(6,7)
# c2.shownumber() 
# c3=c1.add(c2)
# c3.shownumber()         
# c4=c1+c2      #here error because no logic of + in our class so make it dunder function
# c4.shownumber()
# c5=c1-c2      #here error because no logic of - in our class so make it dunder function
# c5.shownumber()