# subject= {        # in the dircnary one is key any its value
#     "phy" : "90",    #we can store  string as value
#     "math": "70",
#     "cs" :"80",          #mostly we use striung as key
#     "num" : 123 ,      #we can store integer as value
#      "pren":"60.6",     #we can store flaoting  value
#      "res":True,          #we can store boleen  value
#      13:123,                #we can use number as key
#      14.6:567 ,               #we can use floting value as key
#      "(x,y)": [1,4],           #only tupal use as key not list  

# }
# print("dictionary subject is\n",subject)
# print(" data type of dictionary  subject\n",type(subject))

# #we can list and tupal in dictionary
# info={
#     "sub":["phy",80,"cs",90],
#     "pl":("py","cpp","java"),
#     "num":123,   
# }
# print("dictionary info is\n",info)

# # dictionary is muteable means we can change 
# #  same keys in one dictionary not allowed
# print("value of key sub\n",info["sub"])  # we can access value by keys 
# print("value of key pl\n",info["pl"])
# info["num"]=456
# print(" updated value of key num\t",info["num"]) #change value of numkey
# info["num2"]=789
# print(" Add new key num2 in info and value \n",info["num2"]) #add a key
# myDic={}
# print("null dictionary\n",myDic)
# myDic["name"]="mohsan"
# print(" Add name in null dictionary\n",myDic)

#                                            #nested dictionary
# student={
#     "name":"Ali",
#     "subject":{
#         "phy":90,
#         "cs":80,
#         "math":70,

#     }
# }
# print("student dictionary is\n",student)
# print(" sub dictionary subject is\n",student["subject"])
# print("value of phy in sub dictionary subject   is\n",student["subject"]["phy"])
# student["subject"]["phy"]=33
# print(" updated value of phy in sub dictionary subject   is\n",student["subject"]["phy"])

#                                       #function of dicnary
# data={
#     "name":"mohsan",
#     "age":19,
#     "subject":["math","cs","eng"],
#     "marks":(80,70,90),

# }
# print("kyes of data dictionary is\n",data.keys())
# print("length of data dictionary is\n",len(data))   #total number of kyes
# print("All values of kyes  in data dictionary is\n",data.values())
# print("type cast values as a list of data dictionary is\n",list(data.keys()))
# print("Return value  age kye   with get function in data dictionary is\n",data.get("age")) #it not give any error 
# print("Return value  age kye   with use of key in data dictionary is\n",data["age"])  #it give error it key ont present
# data.update({"age":"20"})
# print("update value  age kye in data dictionary is\n",data)
# data.update({"height":"5.7"})
# print("Add  value kye by update function in data dictionary is\n",data)

#Question
# word={          #store word meaning
#     "table":["a pice of furniture","list of facts and figure"],
#     "cat":"a small animal",
# }
# print("a list of word meaning:\n",word)
#   #store number in  dictionary
# numDic={}
# s1=input("Enter your first subject \t ")
# n1=int(input("Enter your first subject number\t "))
# s2=input("Enter your second subject \t ")
# n2=int(input("Enter your second subject number\t "))
# s3=input("Enter your third subject \t ")
# n3=int(input("Enter your third subject number\t "))
# numDic[s1]=n1
# numDic[s2]=n2
# numDic[s3]=n3
# print("list of your marks\n",numDic)