a,b= map(int(input().split()))
irregular=[]
for i in range(0,a):
    irre=input().split()
    irregular.append(irre)
for j in range(0,b):
    p=input()
    if irregular.count(p):
        x=irregular.index(p)
        print(irregular[x+1])
    elif p.rindex('y')== 0:
        p=p.pop()
        p.append('ies')
    elif