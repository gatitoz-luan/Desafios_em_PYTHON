meses=[0,31,28,31,30,31,30,31,31,30,31,30,31]
a,b = input().split()
c,d = input().split()
a,b,c,d = int(a),int(b),int(c),int(d)
x=0
if b==d:
    x=c-a
else:
    for z in range(b,d):
        if z==b:
            x+=(meses[b]-a)
        else:
            x+=meses[z]
    x+=c
print(x)