a=int(input("enter number"))
i=0
list=[]
while i<a:
    n=int(input("enter"))
    list.append(n)
    i+=1
print(list)  
list.pop(-2)  
print(list)