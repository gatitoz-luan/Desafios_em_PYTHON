while True:
    x,y = int(input)
    x,y = int(x), int(y)
    if x==0 or y==0:
        break
    elif x>0:
        if y>0:
            print('primeiro')
        else:
            print('quarto')
    else: 
        if y>0:
            print('segundo')
        else:
            print('terceiro')
    
c=0
while True:
    n=int(input)
    x0=y0=0
    for i in range(0,n):
        x,y,x1,y1= map(int, input().split())
        x0