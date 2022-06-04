a = input("Enter a string with letters and integers ")
b = 0
for i in a:
    if(i.isdigit()):
        b = b + int(i)
print("Sum of integers are", b)
