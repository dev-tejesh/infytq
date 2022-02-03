s=input()
req=""
spec=[]
for i in s:
    if i.isalpha():
        req+=i
    else:
        a=s.index(i)
        spec.append(a)
b=req[::-1]
ans=""
for i in range(0,len(b)):
    if i==a:
        ans+=(s[i])
        ans+=b[i]
    else:
        ans+=b[i]
print(ans)

