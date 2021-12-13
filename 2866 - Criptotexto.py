n = int(input())
for i in range(n):
    s = input()
    res=''
    for i in s:
        if i.islower():
            res += i
    print(res[::-1])

