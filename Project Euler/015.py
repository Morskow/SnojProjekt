# bolj ali manj splosno znana zadeva:
# imamo 40 korakov, od tega jih bo 20 desno in 20 dol,
# preostane nam le se, kako jih bomo razporedili.
# poleg direktnega kombinatoricnega izracuna sicer deluje rekurzija,
# ampak traja precej dolgo.

def fakulteta(n):
    if n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

def binom(n, k):
    return (fakulteta(n) // (fakulteta(k) * fakulteta(n-k)))

print(binom(40, 20))
