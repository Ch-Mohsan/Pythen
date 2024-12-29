# tupal is like list but immuteable means conmot nakes changes
tup=(1,2,3,5)
print("data type of tup is\t",type(tup))
print("Access 0th index is\t",tup[0])
print("Access 2th index is\t",tup[2])
#tup[3]=6  assigning value not allowed it means immuteable

#types of tupal
a=()      #empty tupal
print("empty typal\t",a)
b=(1)        #not a signal element tupal like as integer
print("data type of tupal b is like integer\t",type(b))
c=(1,)        #it is a signal element tupal 
print("tupal c  is like signal element tupal\t",type(c))

#tupal slicing
t=(1,2,3,4,5)
print("element of tupal  t form 1 inedex to 4 \t",t[1:4]) # last index not include

#function of tupal
t1=(1,2,4,5,3,6,3,5,)
print(" return the index of number3 \t",t1.index(3))
print(" return the occurance of number3 \t",t1.count(3))


