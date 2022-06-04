import math

def calculator(a):
    print(eval(a))

def cal(a,o,b):
    if(o == '*'):
        print(a*b)
    elif(o == '/'):
        print(a/b)
    elif(o == '+'):
        print(a+b)
    elif(o == '-'):
        print(a-b)
    else:
        print("Invalid operator")

x = input("Select mode auto/manual: ")

if(x == "auto"):
    y = input("Enter the expression: ")
    calculator(y)
    
elif(x == "manual"):
    a = float(input("Enter first number: "))
    o = input("Enter operator")
    b = float(input("Enter second number"))
    cal(a,o,b)
    
else:
    print("Invalid Mode")
