# funkcija, ki presteje stevilo korakov (zacetno stanje se ze steje kot korak)

def collatz(stevilo, n = 1):
    if stevilo == 1:
        return n
    elif stevilo % 2 == 0:
        return collatz(stevilo // 2, n + 1)
    else:
        return collatz(3 * stevilo + 1, n + 1)

# sedaj naredim seznam korakov in poiscem indeks najdaljsega

dolzine = []

for vsa in range(1, 1000001):
    dolzine.append(collatz(vsa))

print(dolzine.index(max(dolzine)) + 1)
