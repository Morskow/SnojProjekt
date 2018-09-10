a = 1
b = 1
c = 0
vsota = 0

while a + b < 4000000:
    c = a + b
    if c % 2 == 0:
        vsota += c
    a = b
    b = c

print(vsota)
