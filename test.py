x= int(input("enter a number"))
if x%2 !=0:
    print("weird")
elif x in range(2,6):
    print("not weird")
elif x in range(6,21):
    print("weird")
else:
    print("not weird")
