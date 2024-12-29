#set is muteable but element of set is immuteable
#we cant store list and dictionary just tupal
coll={1,2,3,3,4,5,5,"a","b","a"}
print("data type of coll is\n",type(coll))    #set is unordered
print("set coll\n",coll)            #set count same element at once
print("length is All unique is\n",len(coll)) 

collection={}         #not a valid empyty set
print("data type of collection is\n",type(collection)) 

collection1= set()       #not a valid empyty set
print("data type of collection is\n",type(collection1)) 
#function of set
data={1,2,3,5.5,"a","b",}
print("data set is\n",data)
data.add(7.8)
print("after add 7.8 data set is\n",data)
#data.add([6,9]) we cant store list in set because its value can be change
data.add((9,0))
print("after add a tupal (9,0) in data set is\n",data)
data.remove(2)
print("after remove 2 data set is\n",data)
data.pop()
print("after remove a remdom data set is\n",data)
data1=data.copy()
print("Make a coppy of data set in anoth set is data1 is\n",data1)
data.clear()
print("after clear  data set is\n",data)

#uniou of set
s1={1,2,3,5,"a","b","c"}
s2={2,3,5,"b","c"}
print("uniou of set1 and set2\n",s1.union(s2))
print("intersetion  of set1 and set2\n",s1.intersection(s2))

#Question
sub={"py","java","c++","py","js","java","py","java","c++","c"}
print("total number of requried class rooms\n",len(sub))
# store 9 and 9.0 in list as sparate
s={9,9.0}                #treat as same in set
print("same number\n",s)          #output only 9
set3={9,"9.0"}                    #store as a string
print("same value in set\n",set3)   
set4={("int",9),("flaot",9.0)}       #store as a form of tupal

