
# with open("my_text.txt","w") as f:
#     f.write("its me!")

# with open("my_text.txt","r") as f:
#     data=f.read()
#     print(data) 

# with open("my_text.txt","a") as f:
#     f.write("\tCh mohsan ali")

# with open("my_text.txt","w+") as f:
#     f.write("hi python!")
#     data=f.read()
#     print(data)

# with open("my_text.txt","r+") as f:
    
#     data=f.read()
#     print(data)
#     f.write("hi java!")

# with open("my_text.txt","a+") as f:
    
#     data=f.read()
#     print(data)
#     f.write("hi java!")

##Question

# with open("my_text.text","w")as f:
#  f.write("Hi everyone\nwe are learing file i/o\nwith java\ni like programing in java")

# with open("my_text.text","r+")as f:
#  data=f.read()
# newdata=data.replace("java","python")
# print(newdata)
# with open("my_text.text","w")as f:
#  f.write(newdata)

# def check_word():
    
#     with open("my_text.text","r+")as f:
     
#       data=f.read()
      
#     if("learing" in data):
#        return True
      
#     else:
#         return False

# print(check_word())

# def check_line():
 
#     data=True
#     line_no=1
#     with open("my_text.text","r") as f:
#      while data:
#       data=f.readline()
#       if("learing"in data):
#         return line_no
#       else:
#         line_no+=1

# print(check_line())       

def find_num():
 count=0
 with open("my_text.text","r") as f:
  data=f.read()
  
  num=list(data.split(","))
  for i in num:
   if(int(i)%2==0):
     count+=1
 print(count)
  
find_num()