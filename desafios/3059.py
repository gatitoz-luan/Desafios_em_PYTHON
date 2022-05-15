n,i,f = map(int, input().split())          #numero de itens da lista, soma minima e maxima
lista = list(map(int,input().split()))      #lista de itens a serem somados
c=0                             #contador de somas na seleção

for x in range(0,n):            #primeiro numero da soma
    for j in range(x, n):       #segundo numero da soma
        if lista[x] != lista[j]:    #para não somar com o proprio
            if lista[x] + lista[j] >=i and lista[x] + lista[j] <=f:     #soma resultar na faixa selecionada
                c +=1
print(c)
