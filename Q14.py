def gcd(x,y):
    if x<y:
        (x,y) = (y,x)
    if(x%y) == 0:
        return y
    else:
        return (gcd(y, x%y))

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(gcd(a,b))
