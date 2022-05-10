list1 = [[1,4,5],[1,3,4],[2,6]]
i=0
l=[]
sum=[]
while i<len(list1):
    if type(list1[i])==list:
        sum+=list1[i]
        # print(list1[i])
    i+=1
print(sum)
sum.sort()
print(sum)

# Merge k Sorted Lists