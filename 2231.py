while True:
    N,M=map(int,input().split())
    lista=[]
    maior=menor=media=c=0
    c+=1

    if N==0 or 0==M:
        break

    for i in range(N):
        lista.append(int(input()))
    
    for j in range(0,len(lista)-M+1):
        for k in range (M):
            media=+lista[(j+k)]
        media=media/M
        if media>maior:
            maior=media
        if media < menor:
            menor=media
        media=0
    
    print(f"Teste {c}")
    print(f'{menor} {maior}')
    print()
