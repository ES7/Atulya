import random

a = []
for i in range(0,100):
    a.append(random.randint(1,99))
print(a)

c = 0
for i in range(0,100):
    for j in range(i+1,100):
        if(a[i]==a[j]):
            print(a[i])
            c += 1
            break
    if(c!=0):
        break
