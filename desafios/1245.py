listat=[]
listap=[]
while True:
    try:
        n= int(input())
        c=0
        for i in range (0,n):
            var= input().split()
            listat.append(var[0])
            listap.append(var[1])

        for j in range (0,len(listat)):
            for k in range (0,len(listat)):
                if listat[j] == listat[k] and listap[j] != listap[k]:
                    c+=1
                    listat[j]=''
                    listat[k]=''
                
        print(c)
        listat.clear()
        listap.clear()
    except EOFError:
        break