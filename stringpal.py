x=int(input())
y=x
r =0
while x!=0:
    l=x%10
    r=r*10+l
    x =x//10
if r ==y:
    print("palindrome")
else:
     print("not palindrome")
