n = int(input()) #lendo o valor
vetor_posicoes = [0 for i in range(301)] #criando um vetor com todas as possiveis posições e preenchendo de 0's
cont = 0
for i in range(n):
    figuras = int(input())
    if vetor_posicoes[figuras] == 0: # verificando se na determinada posição é igual a 0, ou seja, não possui nenhum numero nela
        vetor_posicoes[figuras] = 1 # caso for igual a 0 aquela posição recebe 1, ocupando o lugar dela
        cont += 1 # por fim somamos um no cont
print(cont) #exibindo o dos numeros sem repetição       
print(n - cont) #exibindo a quantidade de numeros repetidos
