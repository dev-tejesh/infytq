l=[1,2,3]
req=[[]]
for i in range(len(l)+1):
    for j in range(i):
        a=l[j:i]
        if len(a)%2!=0:
            req.append(a)
print(len(req)-1)
        
