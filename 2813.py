n = int(input())
casa=trampo=c=t=0
for i in range(n):
    tempo= input().split()
    if tempo[0]=='chuva':
        if c==0:
            casa+=1
            t+=1
        else:
            c-=1
            t+=1
    if tempo[1]=='chuva':
        if t==0:
            trampo+=1
            c+=1
        else:
            t-=1
            c+=1
print(f'{casa} {trampo}')