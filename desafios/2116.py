import math #importar a biblioteca math
n, m = input().split()
n = int(n)
m = int(m)

def primo(z): #criei uma função onde vai verificar se o número é primo ou não, caso ele não seja será retornado o valor 1, senão retornará o valor 0
    for i in range (2, math.ceil(z ** (1/2)) + 1): #verificando se é primo através da raiz quadrada e depois arredondando
        if z % i == 0: 
            return 1
    return 0

p1 = 0 #declarando a variavel
for i in range (n + 1): # o valor vai começar do 0 e seguir até n, verificando qual deles é primo, e toda a vez, ele vai sendo substituido pelo maior primo
    if primo(i) == 0: #caso o valor retornado da função primo sejá 0, o p1 vai receber o valor de i
        p1 = i 
        
p2 = 0 #declarando a variavel
for i in range (m + 1):  # o valor vai começar do 0 e seguir até m, verificando qual deles é primo, e toda a vez, ele vai sendo substituido pelo maior primo
    if primo(i) == 0: #caso o valor retornado da função primo sejá 0, o p2 vai receber o valor de i
        p2 = i
        
x = p1 * p2 #elaborando a multiplicação entre os primos

print(x) #exibindo a resposta


