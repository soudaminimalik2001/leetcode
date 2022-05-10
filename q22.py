# string to integer
a="4193 with word"
b=a.split()
print(a.split())
i=0
while i<len(b):
    # print(type(b [i]))
    if type(b[i])==str:
        print(int(b[i]))
        break
        i+=1
    
# c="0987654321"
# i=0
# while i < len(b):
#     # print(type(b[i]))
#     print(int(b[i]))
#     if b[i] in c:
#         print(b[i])
#     i+=1

