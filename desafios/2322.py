n = int(input()) #peças
contem = list(map(int, input().split())) 
contem.sort()

for i in range(len(contem)):
    if contem[i] != (i + 1):
        break

if contem[i] == (i + 1):
    i += 1

print(i + 1)
