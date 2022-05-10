a=int(input("enter num:-"))
list=[]
i=0
while i<a:
    l=int(input("enter:-"))
    list.append(l)
    i+=1
print(list)
j=0
x=int(input("enter number:-"))
while j<len(list):
    if list[j]==x:
        print(j)
    j+=1
# q.no34   
    