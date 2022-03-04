tot = 0 #variavel 'tot' vai inciar com 0
x = int(input())
for i in range (x): #vezes que a quantidade de intervalos será executada
    t, v = input().split() #lendo os valores
    t = int(t)
    v = int(v)
    tot = tot + (t * v) #o total receberá toda vez que o programa for executado o último valor da multiplicação entre o tempo e a velocidade
print(tot) #exibir o valor final
