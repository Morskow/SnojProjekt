import euler

seznam = []

for a in range(1, 5 * 9 ** 5):
    produkt = 0
    for stevec in range(len(str(a))):
        produkt += int(str(a)[stevec]) ** 5
    if produkt == a:
        seznam.append(a)

print(euler.vsota_seznam(seznam) - 1)
