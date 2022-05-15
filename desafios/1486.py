matriz=[]
while True:
    a,b,c= map(int,input().split()) #coluna, linhas, minimo
    if a==b==c==0:
        break
    resposta=c1=0 #variaveis para controle
    for i in range(0,b):  #preenchendo a matriz
        v=input().split()
        matriz.append(v)
    for j in range(0,a):  #vasculhando cada coluna individualmente
        for k in range(0,b): #conferindo cada item da coluna
            if c1==0:  #se não estamos olhando um item já conferido
                if matriz[k][j]=='1':   #se o item for 1
                    for k in range(k,b): #confere se os próximos são 1 tambem
                        if matriz[k][j]!='1':
                            break
                        c1+=1
                        if c1==c:   #se atinge C 
                            resposta+=1
            if c1!=0: 
                c1-=1 #controle de repetição
    print(resposta)
    matriz.clear()