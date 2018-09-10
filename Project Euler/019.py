# presteje stevilo dni med (ne vkljucno) 1. 1. 1901 in zacetkom tega leta

def dni_pred_letom(leto):
    if leto == 1901:
        return 364
    elif leto % 4 == 0:
        return 366 + dni_pred_letom(leto - 1)
    else:
        return 365 + dni_pred_letom(leto - 1)
    
# presteje stevilo dni tega leta pred tem mesecem

def dni_pred_mesecem(mesec, leto):
    if mesec == 1:
        return 0
    elif mesec == 3 and leto % 4 == 0:
        return 29 + dni_pred_mesecem(2, leto)
    elif mesec == 3:
        return 28 + dni_pred_mesecem(2, leto)
    elif mesec - 1 in [4, 6, 9, 11]:
        return 30 + dni_pred_mesecem(mesec - 1, leto)
    else:
        return 31 + dni_pred_mesecem(mesec - 1, leto)

# samo zlozim oboje, da je bolj prakticno

def dni_vmes(mesec, leto):
    return dni_pred_mesecem(mesec, leto) + dni_pred_letom(leto)

# ce je stevilo veckratnik 7, je torej takrat bila nedelja

nedelja = 0

for mesec in range(1, 13):
    for leto in range(1901, 2001):
        if dni_vmes(mesec, leto) % 7 == 0:
            nedelja += 1

print(nedelja)
