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