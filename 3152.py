#valores A
x1, y1 = input().split() #lendo os valores
x1 = int(x1)
y1 = int(y1)

x2, y2 = input().split() #lendo os valores
x2 = int(x2)
y2 = int(y2)

x3, y3 = input().split() #lendo os valores
x3 = int(x3)
y3 = int(y3)

x4, y4 = input().split() #lendo os valores
x4 = int(x4)
y4 = int(y4)

#valores B
a1, b1 = input().split() #lendo os valores
a1 = int(a1)
b1 = int(b1)

a2, b2 = input().split() #lendo os valores
a2 = int(a2)
b2 = int(b2)

a3, b3 = input().split() #lendo os valores
a3 = int(a3)
b3 = int(b3)

a4, b4 = input().split() #lendo os valores
a4 = int(a4)
b4 = int(b4)

#aplicando a fórmula para encontrar a area de A, usando o abs para remover o sinal negativo caso tenha
areaA = abs(((x1 + x2 )*(y1 - y2)) + ((x2 + x3)*(y2 - y3 )) + ((x3 + x4)*(y3 - y4)) + (x4 + x1)*(y4 - y1))
#aplicando a fórmula para encontrar a area de B, usando o abs para remover o sinal negativo caso tenha
areaB = abs(((a1 + a2 )*(b1 - b2)) + ((a2 + a3)*(b2 - b3 )) + ((a3 + a4)*(b3 - b4)) + (a4 + a1)*(b4 - b1))


if areaA > areaB: #se a area de A for maior 
    print('terreno A')
else: #caso contrário 
    print('terreno B')
    
