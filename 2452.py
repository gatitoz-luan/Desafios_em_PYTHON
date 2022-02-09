f,r=map(int, input().split())
vetor= input().split()
espaco=cont=0
fita=[]
for i in range(f):
    fita.append('0')

while True:
    if fita.count('0')==0:
        break
    for k in range(len(vetor)):
        if (int(vetor[k])+espaco)<=f and (int(vetor[k])-espaco)>=0:
            fita[int(vetor[k])+espaco]=1
            fita[int(vetor[k])-espaco]=1
    espaco+=1
    cont=+1

print(cont)

tape = []
days = 0
length, n = (int(x) for x in input().split())
seeds = (int(x) for x in input().split())

for x in range(length):
    tape.append(0)

for s in seeds:
    tape[s] = 1

while not all(tape.values()):
    for s in [x for x in tape.keys() if tape[x]]:
        j = s - 1
        k = s + 1
        if j > 0:
            tape[j] = 1
        if k < length + 1:
            tape[k] = 1
    days += 1
print(days)



compr, n = input().split()
compr = int(compr)
n = int(n)
pos_anterior = 0
maxi = pos_anterior-1
pos = input().split()  
for i in range(n): 
    diferenca = (int(pos[i]) - pos_anterior)//2  
    if (diferenca>maxi):
        maxi = diferenca
    pos_anterior = int(pos[i])
if (compr - pos_anterior > maxi):
    maxi = compr - pos_anterior
    
print(maxi)
