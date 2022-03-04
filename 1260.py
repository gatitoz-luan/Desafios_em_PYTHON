''
n = int(input())
input() #Removo a primeira linha entre o número de casos de teste e o primeiro caso de teste
for y in range(n):
    dicio = {} #Guardo no dicionário a quantidade de plantas de cada espécie
    lista = [] #Guardo a lista de todas as espécies para poder ordenar no final
    total = 0 #Armazeno o total de plantas
    while True:
        try:
            especie = input().strip() #Leio a espécie
            if especie == '':
                break
            if not especie in dicio: #Se ainda não tenho a espécie no dicionário
                dicio[especie] = 1 #Adiciono ela no dicionário com quantidade 1
                lista.append(especie) #Adiciono ela também na lista de espécies
            else: #Caso contrário
                dicio[especie] += 1 #Simplesmente somo mais uma planta da mesma espécie
            total += 1 #Somo 1 no total de plantas
        except EOFError:
            break
    
    lista.sort() #Ordeno as plantas em ordem alfabética
    for i in range(len(lista)): #Imprimo na tela seguindo o formato da saída
        print("%s %.4f" % (lista[i], (dicio[lista[i]] / total * 100)))
    
    if y < n-1: #Apenas evito quebrar linha no último caso de teste
        print()

'''
n = int(input())
input()

for i in range(n):
    dicionario = {}
    cont = 0
    while True:
        
        try:
            if i+1 == n:
                
                especie = input()
                if especie == '':
                    break
                elif especie not in dicionario:
                    dicionario.update({especie: 1 })
                elif especie in dicionario:
                    dicionario[especie] += 1
                cont += 1
        except EOFError:
            break
        
        especie = input()
        if especie == '':
            break
        elif especie not in dicionario:
            dicionario.update({especie: 1 })
        elif especie in dicionario:
            dicionario[especie] += 1
        cont += 1

   
    porct = 100 / cont    
    for j in sorted(dicionario):
        if j in dicionario :
            x = 0
            x = (dicionario[j] * porct)
            print('{} {:.4f}'.format(j, x))


    
    if i+1 != n:
        print()
'''
