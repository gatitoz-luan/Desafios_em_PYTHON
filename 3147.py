h, e, a, o, w, x = input().split()
h = int(h)
e = int(e)
a = int(a)
o = int(o)
w = int(w)
x = int(x)

safe = h + e + a + x #somar a quantidade que representa o lado bem
notsafe = o + w #somar a quantidade que representa o lado mal

if safe > notsafe: #se a quantidade que representa o lado bem for maior que a do mal exibir Middle-earth is safe.
    print ('Middle-earth is safe.')
else: #caso o contrario exibir Sauron has returned.
    print ('Sauron has returned.')
