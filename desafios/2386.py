cont=0 #variavel cont começa com 0
a = int(input()) #ler o valor de abertura
n = int(input()) #ler o valor de estrelas
for i in range(n):
    f = int(input()) # ler o valor do fluxo de fotons
    if 40000000 <= (f * a): #se o número de fotons que necessitamos para interpretar for menor ou igual a multiplicação do fluxo de fotons e da abertura
        cont = cont + 1  # cont recebe 1
print (cont) #exibir cont
    
