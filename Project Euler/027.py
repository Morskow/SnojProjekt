import euler

def kvadratna(a, b, n):
    return n ** 2 + a * n + b

seznam = []

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        stevec = 0
        prastevilo = True
        while prastevilo == True:
            if kvadratna(a, b, stevec) < 2:
                prastevilo = False
                break
            elif euler.prastevilo(kvadratna(a, b, stevec)) == False:
                prastevilo = False
                break
            else:
                stevec += 1
        seznam.append(stevec)

print(seznam.index(max(seznam)) // 2001 - 999, seznam.index(max(seznam)) % 2001 - 1000)
print((seznam.index(max(seznam)) // 2001 - 999) * (seznam.index(max(seznam)) % 2001 - 1000))

