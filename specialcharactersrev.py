s = input()
l=[]
for i in s:
    if i.isalpha():
        l.append(i)
l=l[::-1]
for j in s:
    if j.isalpha():
        pass
    else:
        l.insert(s.index(j),j)
print(l)
print("".join(l))