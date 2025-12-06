n=int(input("enter a number: "))
x= 0
y= n
while y>0:
    digit=y%10
    x += digit
    y=y//10
print(x)