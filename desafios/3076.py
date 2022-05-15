# -*- coding: utf-8 -*-
import math  #importar a biblioteca math
while True: #enquanto for verdade o programa será executado
    try:
        x = int(input()) #ler o valor do usuário
        x = math.ceil(x / 100) #dividir o valor do usuário por 100 e usando a função ceil o número sempre arredonda para cima
        print(x) #exibindo o programa
    except EOFError:
        break
