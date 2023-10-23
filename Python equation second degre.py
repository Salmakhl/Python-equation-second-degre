from math import*
a=float(input("entre the first coefficient"))
b=float(input("entre the second coefficient"))
c=float(input("entre the third coefficient"))
d=b*b-4*a*c
if d==0:
    print("the solution is:",-b/2*a)
elif d<0:
    print("the solution is not reel")
else :
    print ("the solutions is :",(-b-sqrt(d))/2*a,(-b+sqrt(d))/2*a)    
