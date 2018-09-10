stevec = 0

for a in range(2):
    for b in range(3):
        for c in range(5):
            for d in range(11):
                for e in range(21):
                    for f in range(41):
                        for g in range(101):
                            if 200 * a + 100 * b + 50 * c + 20 * d + 10 * e + 5 * f + 2 * g <= 200:
                                stevec += 1

print(stevec)
