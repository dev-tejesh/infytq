s=input()
req=[]
lowest=float("infinity")
for i in s:
    if i.isnumeric():
        req.append(i)
# print(req)
req.sort(reverse=True)
b="".join(req)
c=set(b)
d=list(c)
d.sort(reverse=True)
a="".join(d)

print(a)

print(type(a))
l=[0,2,4,6,8]
def check():
    for i in a:
        if int(i) in l:
            return True
            break
            
    else:
        return False
print(check())
out=""
if check():
    for i in a:
        if int(i) in l:
            # print(lowest)
            if int(i)<lowest:
                # print("1")
                lowest=int(i)
    print(lowest)
    ans=a.replace(str(lowest),"")
    print(ans+str(lowest))
else:
    print(-1)






    

