def sort(l,a):
    
    if(a == "asc"):
        l.sort()
    elif(a == "desc"):
        l.sort(reverse=True)
    else:
        pass
    print(l)

l=[]
n = int(input("Enter list size "))
print("Enter list values")
for i in range(0,n):
    l.append(int(input()))
    
a = input("Enter sorting type asc, desc or none: ")
sort(l,a)
