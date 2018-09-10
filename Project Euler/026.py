pozicije = []

def pozicija(imenovalec):
    if imenovalec < 100:
        imenovalec = imenovalec / 1000
    elif imenovalec < 10:
        imenovalec = imenovalec / 100
    else:
        imenovalec = imenovalec / 10
    znaki = []
    a = 0
    stevilo = str(format(1 / imenovalec, '.50f'))
    for znak in stevilo:
        if znak in znaki:
            return stevilo.index(str(znaki[-1])) + 1
            break
        else:
            znaki.append(str(znak))

for imenovalec in range(1, 1001):
    pozicije.append(pozicija(imenovalec))

print(pozicije)
print(str(format(1 / 648, '.50f')))
print(pozicije.index(max(pozicije)) + 1)
