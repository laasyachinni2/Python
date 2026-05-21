#WHILE LOOP
i=100
while i >= 1:
    print(i)
    i -= 1
    
#break
i=1
while i<=5:
    if(i==3):
       break   #leaves the loop
    print(i)
    i+=1
    
#CONTINUE
i=1
while i<=10:
    if(i==7):
        i+=1
        continue  #skips the current iteration
    print(i)
    i+=1
    
#FOR LOOP
nums=[1,7,3,5]
for el in nums:
    print(el)

#USING RANGE
for i in range(5):     #range(stop)
    print(i)
    
for i in range(1,10):   #range(start,stop)
    print(i)

for i in range(1,10,2):  #range(start,stop,step)
    print(i)
    
seq=range(5)
for el in seq:
    print(el)
    
#PASS -->it does nothing
for i in range(5):
    pass  
print("HELLO WORLD")



     
