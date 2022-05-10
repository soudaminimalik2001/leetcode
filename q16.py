nums= [0,0,1,1,1,2,2,3,3,4]
list=[]
c=0
i=0
while i<len(nums):
    if nums[i] not in list:
        list.append(nums[i])
        c+=1
    i+=1
print(list)
print(c)

# Remove Duplicates from Sorted Array
