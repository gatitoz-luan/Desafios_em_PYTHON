# -*- coding: utf-8 -*-
x = int(input()) #ler os valores
y = int(input())
if (x <= 120 and x > 0) and (y <= 120 and y>0): #variação entre 0 a 120
    if x < 6 or y < 6: #Se a idade do x ou do y forem menores que 6, exibi NO
        print('NO')
    elif x >= 18 or y >= 18: #Se a idade do x ou do y foren maiores ou igual a 18, exibi YES
        print('YES')
    elif x >= 14 and y >= 14: #Se a idade do x e do y forem maiores ou igual a 14, exibi YES
        print('YES')
    elif x < 14 or y < 14: #Se tanto o x quanto o y forem menores que 14, exibi NO
        print ('NO')
