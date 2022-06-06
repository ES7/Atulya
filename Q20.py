import itertools
import math

n = 1000000
t = []
def prime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if (n%x) == 0:
            break
        else:
            return n 
			
def cirpirme(n):
    no = str(n)
    for x in range(0,len(no)):
        r = no[x:len(no)] + no[0:x]
        if not prime(int(r)):
            return False
    return True

for x in range(2,n):
    if prime(x):
        if cirpirme(x):
        	t.append(x)

print(t)
