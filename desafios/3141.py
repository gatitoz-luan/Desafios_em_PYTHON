nome = input() #lendo o nome

a = input().split("/") #lendo as datas sem a barra
dia = int(a[0]) #declarando o dia como inteiro 
mes = int(a[1]) #declarando o mes como inteiro
ano = int(a[2]) #declarando o ano como inteiro

b = input().split("/") #lendo as datas sem a barra
dia_ani = int(b[0]) #declarando o dia de nascimento como inteiro
mes_ani = int(b[1]) #declarando o mes de nascimento como inteiro
ano_ani = int(b[2]) #declarando o ano de nascimento como inteiro

if dia_ani == dia and mes_ani == mes: #verificando se os dias e os meses são iguais
    print("Feliz aniversario!")

idade = ano - ano_ani #calculando a diferença entre os anos

if (mes_ani == mes and dia_ani > dia) or mes_ani > mes : #verificando o mes e o dia para validar a idade 
    idade -= 1
#imprimindo o resultado
print("Voce tem {} anos {}.".format(idade, nome))
