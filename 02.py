matriz=[]
while True:
    a,b,c= map(int,input().split())
    if a==b==c==0:
        break
    else:
        resposta=c1=comparador=0
        for i in range(0,b):
            v=input().split()
            matriz.append(v)
        for j in range(0,a):
            for k in range(0,b):
                if comparador==resposta:
                    if matriz[k][j]=='1':
                        comparador=resposta
                        k1=k
                        for k1 in range(k1,b):
                            if matriz[k1][j]!='1':
                                break
                            c1+=1
                            if c1==c:
                                resposta+=1
                else:
                    k+=c1
                    comparador=resposta
                    c1=0    
        print(resposta)
        matriz.clear()