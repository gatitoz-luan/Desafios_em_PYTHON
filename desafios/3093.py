def cond (cartas): # criando uma função para verificar as condições
    cond = ['Q' in cartas,'J' in cartas,'K' in cartas,'A' in cartas] #criando uma lista com todas as minhas condições necessárias
    if all(cond): #caso todas as condições da lista sejam verdadeiras
        print('Aaah muleke') #imprime 'Aaah muleke'
    else: #caso contrário
        print('Ooo raca viu') # imprime 'Ooo raca viu'

n = int(input()) #lendo os valores
for i in range(n):
    cartas = input() #lendo os valores das cartas    
    cond (cartas) #chamando a função
        
        
        
 
