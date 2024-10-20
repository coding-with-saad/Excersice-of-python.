d={}    #empty set
marks = {
    "Saad": 100 ,
    "ali": 27 ,
    "op": 449 ,
    "sabi": 70 ,

}
# print(marks,type(marks))
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Saad": 99,"areesha":100,})
# print(marks)
# print(marks.get("Saad2"))   #print none or value of saad if 2 did not write
# print(marks["Saad2"])       #print value of saad if 2 did not write if 2 write it will give an error
# marks.clear()
marks.popitem()
print(marks)













#sets

# s=set() #empty set
s={1,2,3,1,2,3,4,5,6,7} #no repetition is allowed
print(s)
print(type(s))
# s.add("saad")
# print(s)
s.remove(1)
print(s)