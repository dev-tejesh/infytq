l=list(map(int,input().split(",")))
num1=0
num2=0
s=""
for j in l:
    s+=str(j)
a=s.index("5")
b=s.index("8")
# print(a)
# print(b)

num2=int(s[a:b+1:])
for i in range(len(s)):
    if a<=i<=b:
        pass
    else:
        num1+=int(s[i])
print(num1)
print(num1+num2)

