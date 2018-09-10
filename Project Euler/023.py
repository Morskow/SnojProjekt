# upostevali bomo mejo, podano v nalogi

import euler

def je_abundant(stevilo):
    if euler.vsota_deliteljev(stevilo) > 2 * stevilo:
        return True
    else:
        return False

seznam = []

for stevilo in range(1, 28123):
    if je_abundant(stevilo):
        seznam.append(stevilo)

print("Imam seznam.")

# sestejemo in damo v nov seznam

vsote = []

for stevilo in seznam:
    for drugo_stevilo in seznam:
        vsota = stevilo + drugo_stevilo
        if vsota <= 28123:
            vsote.append(vsota)

print("Imam vsote.")

unikat = list(set(vsote))

print((28123 * (28123 + 1)) // 2 - euler.vsota_seznam(unikat))
