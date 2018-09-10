# Naredili bomo zanimiv zapis:

import euler

stevilo = 999999
zapis = ""

for n in range(9, 0, -1):
    stevec = 0
    while (stevec + 1) * euler.fakulteta(n) <= stevilo:
        stevec += 1
    stevilo -= stevec * euler.fakulteta(n)
    zapis += str(stevec)

stevke = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutacija = ""

for crka in zapis:
    permutacija += stevke[int(crka)]
    stevke.pop(int(crka))

permutacija += stevke[0]
print(permutacija)
