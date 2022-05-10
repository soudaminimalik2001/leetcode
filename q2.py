list=[2,7,11,15]
a=int(input("enter number"))
i=0
# while i<len(list):
#     sum=sum+list[i]
#     if sum==a:
#         print(i)
#     i+=1
# no output
# two sum
# l=[]
while i<len(list):
    sum=0
    j=0
    while j<len(list):
        sum=list[i]+list[j]
        if sum==a:
            print([i,j])
        j+=1
    i+=1
        