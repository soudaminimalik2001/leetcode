a=int(input("enter number:-"))
list=[]
i=0
while i<a:
    x=int(input("enter num:-"))
    list.append(x)
    i+=1
print(list)
n=int(input("enter:-"))
j=0
while j<len(list):
    if list[j]==n:
        print(j)
    j+=1
    
# q.no33