# najprej pretvorimo zadevo v string

potenca = str(2 ** 1000)

# preprosto prestejemo stevke

vsota = 0

for stevka in range(0, 10):
    vsota += stevka * potenca.count(str(stevka))

print(vsota)
