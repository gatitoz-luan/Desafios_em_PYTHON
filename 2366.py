a,b= map(int,input().split())
v = input().split()
z=1
x=42195
for i in range(0,a):
    if i != 0:
        if v[i]>v[-1]+b:
            z=0
            break
    if i==a-1:
        if x>v[i+1]+b:
            z=0
if z==0:
    print('N')
if z==1:
    print('S')