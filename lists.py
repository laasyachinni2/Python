marks = [85,34,87,56,65]
print(marks)
print(type(marks))

# --> LISTS ARE SIMILAR TO STRINGS
#INDEXING
print(len(marks))
print(marks[2])
print(marks[3])
# --> CAN STORE DIFFERENT TYPES OF VALUES IN LISTS
# --> ASSIGNING IS POSSIBLE IN LISTS
student = ["Laasya",45,66]
student[0]="Radha"
print(student) 


#SLICING
nums=[10,20,30,40,50]
print(nums[1:4])
print(nums[:4])
print(nums[1:])

#LIST METHODS
list=[2,3,4,5,6]
list.append(7)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(0,1)
print(list)
list.remove(1) #removes the first seen element
print(list)
list.pop(2) # removes the element at that particular index
print(list)
