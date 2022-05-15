'''fibs = []
a, b = 1, 1
for _ in range(90):
    f = a + b
    a = b
    b = f
    fibs.append(b)
trib = []
for n in fibs:
    if '3' in str(n) or n % 3 == 0:
        trib.append(n)
        
while True:
    try:
        n = int(input())
        print(trib[n-1])
    except EOFError:
        break'''
'''
def Threebonacci(x):
    return (str(x).count("3") > 0 or x%3==0);

while True:
    try:
        n = int(input())
        anterior = 0
        atual = 1
        for i in range(n):
            ant = atual
            atual = anterior + atual
            while (not Threebonacci(atual)):
                anterior = atual
                atual = anterior + atual
        print(atual)
    except EOFError:
        break'''

def Threebonacci(x):
    a = (str(x).count("3") > 0 or x % 3 == 0)
    return a

while True:
    try:
        n = int(input())
        anterior = 0
        novo = 1        
        for i in range(n):
            anterior, novo = novo, anterior + novo
            while not Threebonacci(novo):
                anterior, novo = novo, anterior + novo
        print(novo)
    except EOFError:
        break
