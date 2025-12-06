import math
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
D=b**2-4*a*c
if D<0:
    x1=(-b+math.sqrt(D))/(2*a)
    print("x1=",x1)
    x2=(-b-math.sqrt(D))/(2*a)
    print("x2=",x2)
elif D==0:
    x1=(-b/(2*a))
    print("x1=",x1)
    x2=(-b/(2*a))
    print("x2=",x2)
elif D<0:
    print("no real root")