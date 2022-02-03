n=3
l=[1,2,3]
c=0
for i in range(len(l)+1):
    for j in range(i):
        a=l[j:i]
        if sum(a)%2!=0:
            c+=1
print(c)
