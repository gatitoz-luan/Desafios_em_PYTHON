from functools import reduce
def mdc(a, b):
    if b == 0:
        return a
    z = mdc(b, a % b)
    return z


def mmc(a, b):
    x = a*b // mdc(a, b)
    return x



n = int(input())
buraco = [int(x) for x in input().split()]
    
s = set()
for i in range(n):
    p = i
    t = 1
    while buraco[p] - 1 != i: 
        p = buraco[p] - 1
        t += 1
    s.add(t)
fim = (reduce(mmc, s, 1))
print(fim)


