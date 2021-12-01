c=0
while True:
    c+= 1
    a, b= input().split()
    if a==0 or b==0:
        break
    a,b= int(a), int(b)
    inputs=[]
    lista=[]
    pos=[]
    for i in range(0,b):
        s, r= input().split()
        inputs.append(int(s)) 
        inputs.append(int(r))
    for j in range(1,len(inputs)+1):
        lista.append(inputs.count(j))
    pos=lista.sort(reverse=True)
    print(f'Teste {c}')
    maior= pos[0]
    x=lista.count(maior)
    for h in range(0,x):
        print(f'{lista.index(pos[0])} ', end='')
        lista.remove(pos[0])
    print()
    lista.clear()
    pos.clear()
    inputs.clear()