# file, kjer si sproti definiram funkcije, ki mi bojo prav prisle

# izpis vseh deliteljev nekega naravnega stevila
def delitelji(n):
    assert type(n) == int
    seznam = []
    for delitelj in range(1, n + 1):
        if n % delitelj == 0:
            seznam.append(delitelj)
    return seznam

# izpis vsote deliteljev
def vsota_deliteljev(n):
    vsota = 0
    for element in delitelji(n):
        vsota += element
    return vsota

# bolj splosno, vsota elementov seznama
def vsota_seznam(seznam):
    vsota = 0
    for element in seznam:
        vsota += element
    return vsota

# rekurzivno definirana fakulteta
def fakulteta(n):
    if n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

# prastevilo
def prastevilo(n):
    prastevilo = True
    for delitelj in range(2, int((n ** 0.5))+1):
        if n % delitelj == 0:
            prastevilo = False
            break
    return prastevilo
