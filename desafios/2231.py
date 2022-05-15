while True:
    n, m =  input().split()
    n = int(n)
    m = int(m)
    temperatura=[]
    if n == m == 0:
        break
    maior = menor = soma = teste= 0    
    
    for i in range(m):
        temperatura.append(int(input()))
        soma += int(temperatura[i])
        
    for j in range (n):
        x = soma//m
        teste +=1
        temperatura = int(input())
        soma1 = temperatura[j]
        soma2 = temperatura [j - (int(m))]
        soma += (soma1) - (soma2)
        if (soma > maior):
            maior = (soma/m)
        if (soma < menor):
            menor = (soma/m)

    print(f"Teste {teste}")
    print(f"{maior} {menor}")
    print()
    
