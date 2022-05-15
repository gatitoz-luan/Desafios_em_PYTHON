n = int(input())    #quantidade de crianças
m=f=0               #declarando variaveis
for i in range(n):  #analizando e contando numero de crianças de cada sexo
    crianca = input().split()
    if crianca[1] == 'M':
        m += 1
    if crianca[1] == 'F':
        f += 1
print(f'{m} carrinhos')    #print da quantidade
print(f'{f} bonecas')