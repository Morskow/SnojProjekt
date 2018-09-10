seznam = []

for a in range(2, 101):
    for b in range(2, 101):
        seznam.append(a ** b)

# iz seznama naredimo mnozico, ki nam resi vse probleme

print(len(set(seznam)))
