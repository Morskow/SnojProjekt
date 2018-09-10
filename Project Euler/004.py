def palindrom(stevilo):
    if str(stevilo) == str(stevilo)[::-1]:
        return True
    else:
        return False

seznam = []

for a in range(100, 1000):
    for b in range(100, 1000):
        if palindrom(a * b):
            seznam.append(a * b)

print(max(seznam))
