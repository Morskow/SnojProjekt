# vecinoma samo racunska, ni mi ravno vsec, sicer pa naloga zgleda sprasuje po
# absolutni vrednosti razlike

vsota_kvadratov = 0
vsota = 0

for stevilo in range(101):
    vsota_kvadratov += stevilo ** 2
    vsota += stevilo

print(max(vsota_kvadratov - vsota ** 2, vsota ** 2 - vsota_kvadratov))
