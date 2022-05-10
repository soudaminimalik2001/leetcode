list1=[]
list2=[]
i=0
while i<4:
    l1=int(input("enter num1:-"))
    l2=int(input("enter num2:-"))
    list1.append(l1)
    list2.append(l2)
    i+=1
list3=list1+list2
print(list3)
list3.sort()
print(list3)
list3.pop(0)
list3.pop(-1)
print(list3)
j=0
sum=0
while j<len(list3):
    sum+=list3[j]
    j+=1
print(sum)
a=sum/len(list3)
print(a)

# median
    


    