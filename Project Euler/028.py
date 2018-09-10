preskok = 2
stevilo = 1
stevec = 0
poteza = 2
start = 1
vsota = 1

while poteza <= 501:
    while stevec < 4:
        stevilo += preskok
        vsota += stevilo
        stevec += 1
    stevec = 0
    preskok += 2
    poteza += 1

print(vsota)
