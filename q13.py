a=int(input("enter"))
l1=[]
l2=[]
i=0
while i<a:
    x=int(input("enter"))
    y=int(input("enter"))
    l1.append(x)
    l2.append(y)
    i+=1
print(l1)
print(l2)
m=l1+l2
m.sort()
print(m)

# Merge Two Sorted Lists