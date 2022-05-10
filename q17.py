# remove element
a=int(input("enter:-"))
list=[]
i=0
while i<a:
    x=int(input("enter:-"))
    list.append(x)
    i+=1
print(list)
n=int(input("enter number:-"))
j=0
while j<len(list):
    if list[j]==n:
       list.pop(j)
    j+=1
print(list)
print(len(list))
