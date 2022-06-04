a = int(input("Enter the range : "))
c = 0
for i in range(1,a):
    for j in range(1,a):
        if(i%j==0):
            c+=1
    if(c==2):
        print(i)
    c=0
