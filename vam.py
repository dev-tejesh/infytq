import time
start = time.time()
m = 2
l = [3,2,1,3,4,4]
k =[0]*len(l)
for i in range(len(l)):
    k[i]= l.count(l[i])

while m!=0:
    for i in range(min(k)):
        l.pop(k.index(min(k)))
        k.remove(min(k))
        m-=1
        if m==0:
            break
res =0
k = list(set(l))
for i in k:
    res +=k.count(i)

print(res)
time.sleep(1)       
print(time.time()-start)