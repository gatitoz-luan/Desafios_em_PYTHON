matriz=[]
while True:
    a,b,c= map(int,input().split())
    if a==b==c==0:
        break
    resposta=l=c1=0
    for i in range(0,b):
        v=input().split()
        matriz.append(v)
    for j in range(0,a):
        for k in range(0,b):
            if matriz[k][j]=='1':
                for k in range(k,b):
                    if matriz[k][j]!='1':
                        break
                    c1+=1
                    if c1==c:
                        resposta+=1
                c1=0
    print(resposta)
    matriz.clear()