nums=[1,2,3,2,4,3]
seen=set()
dupes=set()
for num in nums:
    if num in seen:
        dupes.add(num)
    else:
        seen.add(num)
print(list(dupes))