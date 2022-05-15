a,b= map(int, input().split())
d=a
e=a
f=a
for i in range (0,b):
    var= input().split()
    if var[0]=="A":
        var[3]=int(var[3])
        if var[1]=='D':
            d+=var[3]
        elif var[1]=='E':
            e+=var[3]
        elif var[1]=='F':
            f+=var[3]
        if var[2]=='D':
            d-=var[3]
        elif var[2]=='E':
            e-=var[3]
        elif var[2]=='F':
            f-=var[3]
    elif var[0]=="C":
        var[2]=int(var[2])
        if var[1]=='D':
            d-=var[2]
        elif var[1]=='E':
            e-=var[2]
        elif var[1]=='F':
            f-=var[2]
    elif var[0]=="V":
        var[2]=int(var[2])
        if var[1]=='D':
            d+=var[2]
        elif var[1]=='E':
            e+=var[2]
        elif var[1]=='F':
            f+=var[2]
print (f'{d} {e} {f}')