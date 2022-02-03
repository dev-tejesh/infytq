r=int(input())
c=int(input())
# matrix=[]
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j],end=" ")
#     print()
mat1 = [[int(input()) for x in range (c)] for y in range(r)]
print(mat1)
mat2=[[int(input()) for x in range(c) ] for y in range(r)]
print(mat2)
res=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(mat1[i][j]+mat2[i][j])
    res.append(a)
print(res)

 
