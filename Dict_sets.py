#dicts are unordered,mutable,cant enter duplicate keys
dict={
    "key":"value",
    "name":"Laasya",
    "branch":"aiml"
}
print(dict)
print(type(dict))
print(dict["name"])
dict["name"]="Radha"
print(dict)

#NESTED DICT
student={
    "name":"Laasya",
    "subjects":{
        "phy":47,
        "chem":50,
        "math":30
    }
}
print(student["subjects"]["chem"])

#DICT METHODS
print(list(student.keys()))
print(list[0])
print(student.values())
print(student.items())
print(student.get("name"))
student.update

#SETS
#The items in the set are unordered and unique
#A set can store int,float,string,tuple because they are immutable
collection={1,2,2,1}
print(collection)
print(type(collection))

emp_set=set()           #syntx for empty set

#SET METHODS-->sets are mutable but the items are immutable
collection.add(7)
collection.add(8)       #-->add item to set
collection.add((1,4,3))
collection.remove(1)    #-->remove the item from the set
collection.pop()        #-->remove a random item
collection.clear()       #-->clears th set
print(len(collection)) 

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))





