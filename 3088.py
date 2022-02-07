while True:
    try:
        frase= input().split()
        for i in range(0,len(frase)):
            for g in range(len(frase[i])):
                print(frase[i][g],end="")
                
            if i<len(frase)-1:
                if frase[i+1] != ','  or frase[i+1] != '.':
                    print(' ',end="")
        print()
    except EOFError:
        break