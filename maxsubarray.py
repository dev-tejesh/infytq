a =[3,5,8,2,19,12,7,11] 
req=[[]]
for i in range(len(a)+1):
    for j in range(i):
        req.append(a[j:i:])
print(req)