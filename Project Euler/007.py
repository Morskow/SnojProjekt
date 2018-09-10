# pocasno reseto z nekaj ne ravno najlepsimi workaroundi

prastevila = [2]
trenutno_stevilo = 3

while len(prastevila) < 10001:
    je_prastevilo = True
    for element in prastevila:
        if trenutno_stevilo % element == 0:
            je_prastevilo = False
            break
    if je_prastevilo:
        prastevila.append(trenutno_stevilo)
    trenutno_stevilo += 1

print(max(prastevila))
