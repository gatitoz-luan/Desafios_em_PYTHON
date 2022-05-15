ex1, ex2 = 0, 0                         # contadores para o primeiro e segundo exército
n, m, s = map(int, input().split())     # entradas de comprimento, largura do campo e soldados no campo no momento inicial
c = n / m                               # coeficiente angular da linha do rio

for i in range(s):                          # loop para cada soldado
    x, y, h = map(int, input().split())     # entrada de coordenadas(x,y) e habilidade
    if x < y * c:                       # se o soldado está acima do rio
        ex1 += h                        # considera ele no primeiro exercito
    else:                               # caso contrário
        ex2 += h                        # considera ele no segundo exercito

print(f"{ex1} {ex2}")                   # exibe os somatórios