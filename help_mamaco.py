t=0
while True:
    t+=1
    a= int(input())
    if a==0:
        break
    for i in range(0,a):
        x1,y1,x2,y2=input().split()
        x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
        if i==0:
            x3=x1
            y3=y1
            y4=y2
            x4=x2
        else:
            if x3<=x1:
                x3=x1
            if y3>=y1:
                y3=y1
            if x4>=x2:
                x4=x2
            if y4<=y2:
                y4=y2
    print(f'Teste {t}')
    if x3<x4 and y3>y4:
        print(f'{x3} {y3} {x4} {y4}')
    else:
        print('nenhum')
