# probal cim bolj poenostaviti zadevo in izboljsati algoritem od par
# nalog nazaj, da gre cim hitreje skozi

vsota = 0

for stevilo in range(3, 2000001, 2):
    prastevilo = True
    for delitelj in range(2, int(stevilo ** 0.5) + 1):
        if stevilo % delitelj == 0:
            prastevilo = False
            break
    if prastevilo == True:
        vsota += stevilo

print(vsota + 2)
