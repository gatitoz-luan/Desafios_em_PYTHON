while True:
    try:
        frase = str(input())            #lê a frase
        x = frase.replace(" ,", ",")    #tira os espaços
        y = x.replace(" .", ".")        #tira os espaços
        print(y)                        #resposta
    except EOFError:                    #caso fim de testes, encerra o programa
        break