vsota = 0

for stevilo in range(1, 1001):
    vsota += stevilo ** stevilo

print(vsota % (10 ** 10))
