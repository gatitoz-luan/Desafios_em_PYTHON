while True:        
    try:
        F = input() #LÊ O VETOR
        a = F.replace("@", "a") #TROCAR o @ pelo a
        b = a.replace("&", "e") #TROCAR o & pelo e
        c = b.replace("!", "i") #TROCAR o ! pelo i
        d = c.replace("*", "o") #TROCAR o * pelo o
        e = d.replace("#", "u") #TROCAR o # pelo u
        print(e) #resposta descodificada  
    except EOFError:        #caso fim de testes, encerra o programa
        break