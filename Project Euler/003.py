def najvecji_prafaktor(stevilo):
    for delitelj in range(2, stevilo):
        if stevilo % delitelj == 0:
            return najvecji_prafaktor(stevilo//delitelj)
    return stevilo

print(najvecji_prafaktor(600851475143))
        
