n=int(input()) #row input(here we are only using rows and does not column as a input)
a=[] #matrix
for i in range(0,n):
    a.append([int(j) for j in input().split()])
print(a)
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m)):
        print(m[i][j])
#for accessing rows in a matrix
for i in range(len(m)):
    print(m[i])
# a=[]
# for i in m:
#     for j in range(len(i)):
#         a.append(i[j])
# print(a)
# for accessing columns in a matrix
a=0
i=0
col=[]
while a!=len(m):
    for j in m:
        col.append(j[i])
    print(col)
    i+=1
    a+=1
# for accessing diagonal elements
for i in range(len(m)):
    for j in range(len(m)):
        if i==j:
            print(m[i][j])
