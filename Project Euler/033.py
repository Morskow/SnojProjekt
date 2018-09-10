import euler

prod_stevcev = 1
prod_imenovalcev = 1
gcd = 1
nov_ulomek = 1

for stevec in range(10, 100):
    for imenovalec in range(10, 100):
        nov_ulomek = 0
        if stevec % 10 == imenovalec % 10 and imenovalec % 10 != 0:
            nov_ulomek = (stevec // 10) / (imenovalec // 10)
        elif stevec % 10 == imenovalec // 10 and imenovalec % 10 != 0:
            nov_ulomek = (stevec // 10) / (imenovalec % 10)
        elif stevec // 10 == imenovalec // 10 and imenovalec % 10 != 0:
            nov_ulomek = (stevec % 10) / (imenovalec % 10)
        elif stevec // 10 == imenovalec // 10 and imenovalec % 10 != 0:
            nov_ulomek = (stevec % 10) / (imenovalec % 10)
        if stevec / imenovalec == nov_ulomek and stevec < imenovalec:
            prod_stevcev = prod_stevcev * stevec
            prod_imenovalcev = prod_imenovalcev * imenovalec
            print(stevec, imenovalec)
 
for delitelj in euler.delitelji(prod_stevcev):
    if prod_imenovalcev % delitelj == 0:
        gcd = delitelj

print(str(prod_stevcev // gcd) + "/" + str(prod_imenovalcev // gcd))
