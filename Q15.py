string = input("Enter a string : ")
a = d = s = 0

for i in range(len(string)):
    
    if(string[i].isalpha()):
        a += 1
    elif(string[i].isdigit()):
        d += 1
    else:
        s += 1
        
print("\nTotal Number of Alphabets in the string is", a)
print("Total Number of Digits in the string", d)
print("Total Number of Special Characters in the string", s)
