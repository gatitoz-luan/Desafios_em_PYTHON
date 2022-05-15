n = int(input()) #lendo os casos de testes
for i in range(n):
    linha = input().split()  #lendo as dimensoes
    medidasA = [int(linha[0]), int(linha[1]), int(linha[2])] #declarando as tres primeiras dimensões para a variavel dimensoesA
    medidasB = [int(linha[3]), int(linha[4]), int(linha[5])] #declarando as tres ultimas dimensões para a variavel dimensoesB
    #colocando elas em ordem
    medidasA.sort()
    medidasB.sort()
    
    #se as duas condições forem verdadeiras, ele vai imprimir 3
    if (medidasB[2] > medidasA[1] and medidasB[1] > medidasA[0]) and (medidasA[2] > medidasB[1] and medidasA[1] > medidasB[0]):
        print('3')
        
    #se a somente a primeira condição dor verdadeira, ele vai imprimir um
    elif medidasB[2] > medidasA[1] and medidasB[1] > medidasA[0]:
        print('1')
        
    #se a somente a segunda condição dor verdadeira, ele vai imprimir dois       
    elif medidasA[2] > medidasB[1] and medidasA[1] > medidasB[0]:
        print('2')
    #caso nenhuma condição seja verdadeira, ele imprime zero   
    else:
        print('0')
    
    
