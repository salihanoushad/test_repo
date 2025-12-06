lst=["zero","one","two","three","four","five","six","seven","eight","nine"]
x=input("enter number:")
for i in x:
    if i=="-":
        print("minus",end="")
    else:
        print(lst[int(i)],end="")
