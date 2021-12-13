n= int(input())
lista=[]
for i in range (0,n):
    c=0
    pe= input().split()
    lista.append(pe)
    for j in range (i,-1,-1):
        if lista[j][0].count(pe[0])==1:
            if lista[j][1].count(pe[1])!=1:
                c+=1
                lista.remove(lista[i])
                lista.remove(lista[j])