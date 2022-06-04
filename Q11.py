s = input("Enter a string: ")
a = ''
for i in s:
    a=i+a
if(s==a):
    print("pallindrome")
else:
    print("not a pallindrome")
