s=input()
a=s.split(",")
print(a)
print(a[0])
print(a[1])
l=[]
for i in a:
    su=0
    for j in i:
        if j.isnumeric():
            # print(j)
            su+=(int(j)**2)
    l.append(su)
strings=[]
for k in a:
    string=""
    for m in k:
        if m.isalpha():
            string+=m
    strings.append(string)
print(strings)
req=""
for i in range(len(l)):
    if l[i]%2==0:
        req+=strings[i][-1]+strings[i][0:len(strings[i])-1]
    else:
        req+=strings[i][2:len(strings[i]):]+strings[i][0:2:]
    req+=" "
print(req)
            
        

    

        
    


    