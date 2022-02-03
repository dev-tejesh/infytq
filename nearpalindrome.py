num=int(input())
a=num
while num!=int(str(num)[::-1]):
    a+=1
    if a==int(str(a)[::-1]):
        print(a)
        break
