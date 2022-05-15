tot = 0 #variavel 'tot' vai inciar com 0
z = int(input())
for i in range (z): #vezes que a quantidade de intervalos será executada
    x, y = input().split() #lendo os valores
    x = int(x)
    y = int(y)   
    tot = (x*y)//2 #o tot receberá a multiplicação os dois bambus e depois será dividida por 2, já que a cruz indica a metade deles 
    print('{} cm2'.format(tot))
    
