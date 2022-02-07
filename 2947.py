q=int(input())
d=input()
a=int(input())
p=[]
cont=contador=0

for i in range(a):
    p.append(input())

for f in range(a):
    for x in range(q):
        if p[f][x] != d[x]:
            cont+=1
    if cont>contador:
        contador=cont
    cont=0

print(contador)