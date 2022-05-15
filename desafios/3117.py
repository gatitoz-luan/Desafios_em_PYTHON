tot,min=map(int, input().split())   #alunos e o minimo necessário
chega= input().split()  #Tempo de chegada de cada aluno
atrasos=0           #contador

for i in range(tot):    #contando o numero de atrasos
    if int(chega[i]) > 0:
        atrasos += 1

if (tot-atrasos)>min:   #condição de tem muitos atrasados
    print('NO')
else:
    print('YES')