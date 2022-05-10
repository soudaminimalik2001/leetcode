list=[3,7,-1,8,10]
list.sort()
print(list)
a=int(input("enter number"))
i=0
while i<len(list):
    if a==list[i]:
        print(i)
    # else:
    #     print(-1)
    #     break
    i+=1
# binary