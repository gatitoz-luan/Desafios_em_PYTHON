teclado = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"} #criando o teclado do aparelho
repeticao = [] #criando a lista onde serão armazenados as teclas repetidas

def verifica(frase): #criando a função
    x = len(frase)
    for i in range(x):
        #criando algumas variaveis que serão utilizadas para armazenamento
        maiusc = ''
        espaco = ''
        asterisco = ''
        string = ' '
        final = ''
        cont = 1
        for j in teclado:
            #lendo as letras minusculas 
            if(frase[i].lower() in teclado[j]): # transformando a letra em minuscula para achar no dicionario criado
                string = str(teclado[j])
                final = j # passamos a posição para a variavel final 
                break
        z = len(string)
        for k in range(z):
            #lendo os espaços
            if(frase[i] == " "): #caso tenha algum espaço 
                espaco = '0' #a variavel espaço vai receber 0
            #lendo as letras maiusculas
            if(frase[i] == string[k].upper() and espaco != '0'): #caso tenha alguma letra maiuscula
                maiusc= '#' # a variavel vai receber o #
            if(frase[i].lower() != string[k]): # caso tenha letra minuscula na string
                cont += 1 # contando a quantidade de vezes que é necessário passar, até chegar na letra
            else:
                break
        if(i == 0): #caso nossa palavra seja 0  
            repeticao = final 
        elif(repeticao == final and maiusc != '#' and espaco != "0"): #verificando o intervalo de tempo caso ele obedeça ao que é pedido 
            asterisco = '*' #se sim, ele vai receber *
        else:
            repeticao = final            
        print(maiusc, espaco, asterisco, '{}'.format(final) * cont, end='', sep='') #imprimindo o resultado
    print(end='\n')
    
mensagens = int(input()) #lendo a quantidade de mensagens a receber 
for x in range(mensagens):
    frase = input() #lendo a frase ou palavra
    verifica(frase) #chamando a função
    

