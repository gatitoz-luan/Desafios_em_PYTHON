
resultado = 0                         
K = int(input())                  # numero de questões
resQ = [""] * K                   # Criando espaços em lista para as respostas
resD = input()                    # prova do desafortunado
N = int(input())                  # numero de alunos

for _ in range(N):                # Loop das respostas dos outros alunos
    resA = input()                # Input da resposta de cada aluno
    for i in range(len(resA)):    # Loop para comparar respostas
        if resA[i] != resD[i]:    # checa se são diferentes
            resQ[i] += resA[i]    # Adiciona a letra na string da questão

for t in resQ:      # Loop para saber qual é a letra que mais repete por questão
    aList = []                  # Lista para as alternativas
    lFreq = []                  # Lista de frequência
    for z in t:                 # em cada alternativa
        if z in aList:          # se tiver na lista de alternativas
            lFreq[aList.index(z)] += 1  # Incrementa a Lista de frequência
        else:
            aList.append(z)     # se não tiver na lista de alternativas ele é adicionado 
            lFreq.append(1)     # Incrementa a Lista de frequência
        
    if len(lFreq) > 0:          # verifica se a lista está vazia
        resultado += max(lFreq)       # Soma o mais frequente
    
print(resultado)  


