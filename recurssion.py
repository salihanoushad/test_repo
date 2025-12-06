def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
x=int(input("enter a number:"))
print(factorial(x))