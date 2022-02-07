flavinho = input().split() #aposta
sorteado = input().split() #comparação
resultado = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']
res = 0

for i in flavinho:
    if i in sorteado:
        res += 1    #Contagem de acertos

if res == 6:    #condição para resposta
    print('sena')
elif res == 5:
    print('quina')
elif res == 4:
    print('quadra')
elif res == 3:
    print('terno')
elif res < 3:
    print('azar')
