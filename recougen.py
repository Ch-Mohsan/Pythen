# def num(n):
#   if(n==0):
#     return
    
#   print(n)
#   num(n-1)
     
# num(5)
# def fact(n):
#   if(n==0 or n==1):
#     return 1
  
    
  
#   return fact(n-1)*n
  
 


# def sumofn(n):
#   if(n==0 or n==1):
#     return 1
  
    
  
#   return sumofn(n-1)+n
  
# number=int(input("Enter number\t"))  
# print("factorial\t",sumofn(number))

def p_list(lis,id=0):
  if(id==len(lis)):
    return
  print("value of list\t",lis[id])
  p_list(lis,id+1)
list=["a","b","c","d"]
p_list(list)