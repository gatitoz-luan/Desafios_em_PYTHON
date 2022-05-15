while True:
    try:
        a= str(input("Que horas são? "))
        #a= str(input())  reativar e apagar linha acima
        hora= int(a[0]+a[1])
        min= int(a[3]+a[4])
        print('Em seu relógio de conversão binária está da seguinte forma:') #apagar pra pôr no uri
        print(" ____________________________________________")
        print("|                                            |")
        print("|    ____________________________________    |_")
        print("|   |                                    |   |_)")
        print("|   |   8         4         2         1  |   |")
        print("|   |                                    |   |")
        print("|   |   ",end="")
        
        if hora/8>=1:
            print("o         ",end="")
            hora-=8
        else:
            print("          ",end="")
        if hora/4>=1:
            print("o         ",end="")
            hora-=4
        else:
            print("          ",end="")
        if hora/2>=1:
            print("o         ",end="")
            hora-=2
        else:
            print("          ",end="")
        if hora==1: 
            print("o  ",end="")
        else:
            print("   ",end="")
        
        print("|   |")
        print("|   |                                    |   |")
        print("|   |                                    |   |")
        print("|   |   ",end="")
        
        if min/32>=1:
            print("o     ",end="")
            min-=32
        else:
            print("      ",end="")
        if min/16>=1:
            print("o     ",end="")
            min-=16
        else:
            print("      ",end="")
        if min/8>=1:
            print("o     ",end="")
            min-=8
        else:
            print("      ",end="")
        if min/4>=1:
            print("o     ",end="")
            min-=4
        else:
            print("      ",end="")
        if min/2>=1:
            print("o     ",end="")
            min-=2
        else:
            print("      ",end="")
        if min==1:
            print("o  ",end="")
        else:
            print("   ",end="")
        print("|   |")
        print("|   |                                    |   |")
        print("|   |   32    16    8     4     2     1  |   |_")
        print("|   |____________________________________|   |_)")
        print("|                                            |")
        print("|____________________________________________|")
        print()
    except EOFError:
        break
        