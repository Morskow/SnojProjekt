# program se izvede veliko krajše, ker se lahko znajdemo s formulo in
# dejstvom, da sta sosednji števili tuji

def delitelji(stevilo):
    deli = 0
    for delitelj in range(1, stevilo + 1):
        if stevilo % delitelj == 0:
            deli += 1
    return deli

def del_trikotnega(stevilo):
    if stevilo % 2 == 0:
        return delitelji(stevilo // 2) * delitelji(stevilo + 1)
    else:
        return delitelji(stevilo) * delitelji((stevilo + 1) // 2)

stevilo = 1

while del_trikotnega(stevilo) <= 500:
    stevilo += 1

print(stevilo * (stevilo + 1) // 2)
