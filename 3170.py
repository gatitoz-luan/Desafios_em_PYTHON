b = int(input())
g = int(input())

x = g//2 #o 'x' vai dividir a quantidade de galhos em metade

if x > b: # se a metade de galhos for maior que o numero de bolinhas
    tot = x - b #então a variavel 'tot' vai diminuir o a metade de galhos pelo numero de bolinhas para saber quanto falta 
    print('Faltam {} bolinha(s)'.format(tot)) #e então vai exibir a quantidade que falta
else: #caso contrário será exibido a mensagem que ela já tem todas as bolinhas
    print('Amelia tem todas bolinhas!')
