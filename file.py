import os

# with open("demo.txt","r") as f: #open for read data from file
#       data=f.read()
# print(data)
# with open("demo.txt","r") as f: #open for read data from file
#       data=f.read(5)             #just read first five char 
# print(data)
# with open("demo.txt","r") as f: #open for read data from file
#       line1=f.readline()
#       line2=f.readline()  #if read data one time and then read line it  is empty
# print(line1)                        #read line by line
# print(line2)

#     #write mood create new write text file automatically

# with open("write.txt","w") as f: #open for writ data on file which  exist already
#     f.write("python\njava\tcpp\nJs")    # write mood over write all the data 

# with open("write.txt","a") as f: 
#     f.write("\n cood with herry\napna college")    #apend mood add data at the end

# with open("demo.txt","a") as f: 
#     f.write("\n Now i have complete 3rd samester")    #apend mood add data at the end

# with open("write.txt","r+") as f: 
#     f.write("my pythen and cpp ")    #r+ mood not over write whole file 
#     data=f.read()                   #read and write at a time
# print(data)     #cursur move next after write data and then read next


# with open("write.txt","w+") as f: 
# #     data=f.read()           #remove all data
# # print(data)     
#     f.write("java script")    #w+ mood  over write whole file write new data


# with open("demo.txt","a+") as f:
#     #data=f.read() #out put is nothing because curser at the end of data
#     f.write("abcdef")
# #print(data)

##os.remove("sampal.text")



##practice Question
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learing file I/O\nwith java\ni live programming in java")
# with open("practice.txt","r") as f:
#     data=f.read()
# newdata=data.replace("java","python")
# print(newdata)
# with open("practice.txt","w") as f:
#        f.write(newdata)

# with open("practice.txt","r") as f:
#     data=f.read()
#     if("learing"in data):
#         print("found")
#     else:
#         print("not found")


# def chec_word():
    
    
#  word="learing"
#  data=True
#  line=1
#  with open("practice.txt","r") as f:
#    while data:
#     data=f.readline()
#     if(word in data):
#          print(line)
#          return
#     line+=1
 
#  return -1  
# print(chec_word())

def find_num():
    count=0
    with open("practice.txt","r") as f:
       data=f.read()
       print(data)
       nums=data.split(",")
       print(nums)
       for val in nums:
           if(int(val)%2==0):
               count+=1
    print("total even number in your data",count)             
find_num()       


