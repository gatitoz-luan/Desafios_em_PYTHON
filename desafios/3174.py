n = int(input()) #lendo a quantidade de elfos
total = 0

dicionario = { 'bonecos': 0,'arquitetos': 0,'musicos': 0,'desenhistas': 0} #criando um dicionario para as profissoes e o tempo de trabalho   

for i in range(n):
    nome, profissao, tempo = input().split() #lendo as variaveis
    tempo = int(tempo) #transformando o tempo em inteiro
    dicionario[profissao] += tempo #o dicionario vai receber o tempo em determinada profissão
#dividindo cada valor do tempo pela determinada quantidade de horas e adicionando na variavel total
total += dicionario['bonecos'] // 8
total += dicionario['arquitetos'] // 4
total += dicionario['musicos'] // 6
total += dicionario['desenhistas'] // 12

print(total)
