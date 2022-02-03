import time
from collections import Counter
m=3
start = time.time()
a=[2,4,1,5,3,5,1,3]
l=Counter(a)
print(l)
d=dict(l)
print(d)
while m!=0:
    for i,j in d.items():
        # print(i)
        # print(j)
        for k in range(j):
            # print(i)
            a.remove(i)
            m-=1
            if m<=0:
            # print("2")
                break
            # print(m)
        if m<=0:
            # print("2")
            break

print(len(set(a))) 
print(time.time()-start)
        




