# 3sum
a=int(input('enter number'))
x=0
y=1
z=0
list=[]
while z<=a:
    list.append(z)
    # print(list)
    x=y
    y=z
    z=x+y
print(list)