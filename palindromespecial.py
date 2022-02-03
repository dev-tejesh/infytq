s=input()
a=True
if s==s[::-1]:
    print(len(s))
else:
    while a:
        a=int(s)
        b=int(s[::-1])
        if str(a+b)==str(a+b)[::-1]:
            print(len(str(a+b)))
            a=False

    