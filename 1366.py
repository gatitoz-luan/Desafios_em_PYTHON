while True:
    a=int(input())
    x=0
    if a == 0:
        break
    for i in range(0,a):
        v = input().split()
        for j in range(0,len(v)):
            v[j]= int(v[j])
        x+=v[1]//2
    print(x//2)