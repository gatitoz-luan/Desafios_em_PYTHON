n=int(input())
par=[]
pares=[]

for i in range(n):
    pontos=iguais=0

    jogo=input().split()
    jogo.sort()
    
    if jogo[0]==jogo[1]:
        par.append(jogo[0])
        iguais+=1
    if jogo[2]==jogo[1]:
        par.append(jogo[0])
        iguais+=1
    if jogo[2]==jogo[3]:
        par.append(jogo[0])
        iguais+=1
    if jogo[3]==jogo[4]:
        par.append(jogo[0])
        iguais+=1

    for j in range(len(par)):
        if par[j] not in pares:
            pares.append(int(par[j]))

    if int(jogo[0])+1==int(jogo[1]) and int(jogo[1])+1==int(jogo[2]) and int(jogo[2])+1==int(jogo[3]) and int(jogo[3])+1==int(jogo[4]):
        pontos+=200
        pontos+=int(jogo[0])
    
    if iguais==1:
        pontos+=pares[0]
    if iguais==2:
        if len(pares)==1:
            pontos+=pares[0]
            pontos+=140
        else:
            pontos+=pares[0]*2
            pontos+=pares[1]*3
            pontos+=20
    if iguais==3:
        if len(pares)==1:
            pontos+=pares[0]
            pontos+=180
        else:
            pontos+=pares[0]
            pontos+=160
    par.clear()
    pares.clear()
    jogo.clear()

    print(f'Teste {i+1}')
    print(pontos)
    print()
