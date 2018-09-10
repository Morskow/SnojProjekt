# precej brute force zadeva, zaradi majhnosti na pol narejena rocno.
# da poenostavim, kolikor mogoce, sem vzel kar produkt vseh prastevil pod 20,
# saj bo gotovo delil iskano.


a = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

def tapravo(stevilo):
    for delitelj in range(1, 20):
        if stevilo % delitelj != 0:
            return tapravo(stevilo + a)
    return stevilo

print(tapravo(a))
