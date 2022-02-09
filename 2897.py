while True:
    res = 0             # Variável do resultado
    ex = []             # histório de comandos 
    n = int(input())    # número de comandos
    if n == 0:          # encerra programa
        break

    cmd = list(map(int, input().split()))   # Lista de comandos

    for i in range(len(cmd)):   # Loop a cada comando
        if cmd[i] in ex:    # se está no histórico
            res += i - ex.index(cmd[i]) # última aparição do comando
            ex[ex.index(cmd[i])] = 0    # troca o comando no histórico por 0 para que não seja achado pelo "index"
            ex.append(cmd[i])   # bota o comando no histórico
        else:
            res += cmd[i] + i   # Calcula o número de passos
            ex.append(cmd[i])   # Adiciona o comando no histórico

    print(res)                  # Exibe o resultado