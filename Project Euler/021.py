# od te naloge dalje uporabljam funkcije, ki sem jih spisal v poseben file, saj se mi dolocene velikokrat ponavljajo

import euler

seznam = []

for stevilo in range(1, 10001):
    par = euler.vsota_deliteljev(stevilo) - stevilo
    if par < 10000 and par != stevilo and euler.vsota_deliteljev(par) - par == stevilo:
        seznam.append(stevilo)
    

vsota = 0

for element in seznam:
    vsota += element

print(vsota)
