# s="abcbbacb"
s =input("enter")
a=list(s)
print(a)
i=0
c=0
list=[]
while i<len(a):
    if a[i] not in list:
        list.append(a[i])
        c+=1
    i+=1
print(list)
print(c)
    
    