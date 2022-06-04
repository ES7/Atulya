import random

a = []
b = int(input("Enter the size of array : "))

for i in range(0,b):
    a.append(random.randint(1,99))
print(a)

c = 0
max = 0
val = 0
for i in range(0,b):
    for j in range(0,b):
        if(a[i]==a[j]):
            c+=1
    if(c>max):
        max = c
        val = a[i]
    c = 0
    
print(val,"repeated",max,"times")
