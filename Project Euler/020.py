# spet malo rekurzije

def fakulteta(n):
    if n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

# se funkcija za vsoto stevk

def vsota_stevk(stevilo):
    vsota = 0
    zapis = str(stevilo)
    for stevka in range(1, 10):
        vsota += stevka * zapis.count(str(stevka))
    return vsota

# pozenemo

print(vsota_stevk(fakulteta(100)))
