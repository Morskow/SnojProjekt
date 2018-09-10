a = 1
b = 2
c = 2
indeks = 3

while len(str(c)) < 1000:
    c = a + b
    a = b
    b = c
    indeks += 1

print(indeks)
