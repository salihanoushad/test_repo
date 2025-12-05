x=int(input("enter a number:"))
s = 0
for i in range(1,(x//2)+1):
    if x%i==0:
       s=s+i
if s==x:
    print("perfect")
else:
    print("not perfect")