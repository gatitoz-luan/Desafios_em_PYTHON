while True:
    n = int(input())
    teste=soma= 0

    for x in (n):
        c = input().split()
        for y in range (len (c)):
            c[y] = int(c[y])
        teste += 1
        
        p0 = c.count(c[0])
        p1 = c.count(c[1])
        p2 = c.count(c[2])
        p3 = c.count(c[3])
        p4 = c.count(c[4])

        #regra 1   
        if (c[0]==c[1]-1) and (c[1]==c[2]-1) and (c[2]==c[3]-1) and (c[3]==c[4]-1):
                soma = 200 + c[0]

        #regra 2
        if p0 == 4 or p1==4 or p2 == 4 or p3 == 4 or p4 ==4:
                soma = 180 + c[1]
    
        
        #regra 3
        elif (p0 == 3 or p1==3 or p2 == 3 or p3 == 3 or p4 == 3) and (p0 == 2 or p1==2 or p2 == 2 or p3 == 2 or p4 == 2):
            soma = 160 + c[4]

        #regra 4
        elif (p0 == 3 or p1==3 or p2 == 3 or p3 == 3 or p4 == 3) and (p0 != p1 or p0 != p2 or p0 != p3 or p0 != p4 or p1 != p2 or p1 != p3 or p2 != p3 or p3 != p4):
            soma = 140 + c[0]

        #regra 5
        elif ((p0 == 2 and p1==2 or p2 == 2 or p3 == 2 or p4 == 2)):
            if (c[0] > c[3]):
                soma = (3 * c[0]) + (2* c[4]) + 20
            else: 
                soma = (3*c[3])+(2*c[0])+20

        elif (((c[0]==c[1] or (c[0]==c[2]) or (c[0]==c[2]) and (c[3]==c[4]))  and c[2]==c[3])):
            if (c[0]>c[2]): 
                soma = 3*c[0]+2*c[2]+20
            else:
                soma = 3*c[3]+2*c[1]+20

        elif ((c[1]==c[2] and c[3]==c[4])): 
            if (c[1]>c[3]):
                soma = 3*c[1]+2*c[3]+20
            else:
                soma = 3*c[3]+2*c[1]+20
        #regra  6
        elif (c[0]==c[1] or c[1]==c[2]): 
            soma = c[1]
    
        elif (c[2]==c[3] or c[3]==c[4]): 
            soma = c[3]

        print('Teste', teste)
        print(soma)
        print()
        