l=["Robert:36787","Tina:68721","Jo:56389"]
empname=[]
empno=[]
req=""
name=""
for i in l:
    for j in i:
        if j.isnumeric():
            req+=j
    empno.append(req)
    req=""
for i in l:
    for j in i:
        if j.isalpha():
            name+=j
    empname.append(name)
    name=""
print(empname)
print(empno)
finstr=""
maxlist=[]
answer=""
for k in range(len(empno)):
    for m in empno[k]:
        if int(m)<=len(empname[k]):
            maxlist.append(m)
    if maxlist==[]:
        answer+="X"
    else:

        ans=max(maxlist)
        # print(ans)
        answer+=empname[k][int(ans)-1]
        maxlist=[]
print(answer)



    

# print(answer)

            


    


    