while True:
    try:

        palavra = input().split()

        for i in range(0, len(palavra)):
            for j in range(len(palavra[i])):
                if palavra[i][j]=='!':
                    print('i', end='')
                elif palavra[i][j]=='@':
                    print('a', end='')
                elif palavra[i][j]=='*':
                    print('o', end='')
                elif palavra[i][j]=='#':
                    print('u', end='')
                elif palavra[i][j]=='&':
                    print('e', end='')
                else:
                    print(palavra[i][j], end='')
            print(" ", end='')
        print('',end='\n')
    except EOFError:
        break