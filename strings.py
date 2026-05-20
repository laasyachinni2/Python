#Strings are immutable
#once assigned can not changed

str1="Laasya"
str2="chinni"
#(1) INDEXING-can acess but canot assign
print(str1[2])
print(str1[3])
#str[0]=r X

#SLICING
str="radhakrishna"

print(str[1:4])
print(str[:4]) 
print(str[1:])

#String FUNCTIONS
str="one for all and all for one"

print(str.endswith("ne"))
print(str.capitalize())
print(str.replace("one","Many"))
print(str.find("n"))
print(str.count("l"))
