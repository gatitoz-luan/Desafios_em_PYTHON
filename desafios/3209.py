   
m = int(input()) #lendo os casos de testes
for i in range (m):
    soma = 0
    o = input().split(" ") #lendo os valores em formato de lista
    k = int(o[0]) #declarando para k o valor do a0
    outros = (o[1:]) #a variavel outros fica com o resto dos valores 
    for i in outros: #somando todos os valores    
        soma += int(i)
    x = soma - k + 1 #diminuindo a soma dos valores por k e depois somando com 1     
    print(x) #imprimindo o resultado
