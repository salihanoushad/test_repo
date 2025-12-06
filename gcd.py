x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x < y:
x, y = y, x
while y != 0:
x, y = y, x % y
print(x)