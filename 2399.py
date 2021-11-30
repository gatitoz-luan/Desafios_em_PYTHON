while True:
    try:
        n=int(input())
        if n==0:
            break
        lista=[]
        for i in range(0,n):
            a=int(input())
            lista.append(a)
        for j in range(0,n):
            if j==0 and n>1:
                print(lista[j]+lista[j+1])
            elif j==n-1:
                print(lista[j-1]+lista[j])
            else:
                print(lista[j-1]+lista[j]+lista[j+1])
    except EOFError:
        break