piramida = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

seznam = []

for polnilo in range(15):
    seznam.append([])

for indeks in range(len(piramida)):
    if piramida[indeks] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and piramida[indeks + 1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        for podseznam in range(len(seznam)):
            if len(seznam[podseznam]) <= podseznam:
                seznam[podseznam].append(int(piramida[indeks : indeks + 2]))
                break

# gremo kar brute force

def max_dolzina(pozicija = 0, n = 0):
    if n == 14 and pozicija < 14:
        return max(seznam[n][pozicija], seznam[n][pozicija + 1])
    elif n == 14:
        return seznam[14][14]
    else:
        return seznam[n][pozicija] + max(max_dolzina(pozicija, n + 1), max_dolzina(pozicija + 1, n + 1))

print(max_dolzina())
