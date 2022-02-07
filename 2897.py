while True:
    n=int(input())
    if n == 0:
        break
    cont=0
    var= input().split()
    for i in range(n):
        if var.count(var[i])>1:
            
        cont+=int(var[i])
        cont+=i
    print(cont)
