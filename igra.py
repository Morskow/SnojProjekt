import random
import os

# Definiramo sezname črk, ki jih bomo uporabili v ključu, in slovar za posamezne črke
seznam = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
male = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
obstojeci = []
restart1 = []
slovar = {}
letterfreq="Frekvenca črk: E, T, A, O, I, N, S, R, H, D"

# Odpremo seznam s stavki
stavki = open("stavki.txt", "r")

# Naključno izberemo stavek
lines = stavki.readlines()
niz = lines[random.randint(-1, 49)][:-1]
niz1 = niz.strip()
niz2 = niz
seznam_crk=[]

# Posodobimo slovar z naključno izbrano permutacijo velikih črk
for letter in niz:
    if letter in seznam_crk or letter == " ":
        continue
    else:
        seznam_crk.append(letter)
        slovar[letter]=random.choice(seznam)
        seznam.remove(slovar[letter])
        obstojeci.append(slovar[letter])
    restart2 = obstojeci

# Šifriramo izbrani stavek po slovarju
for letter in niz:
    if letter not in slovar:
        continue
    else:
        niz = niz.replace(letter, str(slovar[letter]))
    nizr = niz

# 
restart = niz
print(niz)
print(" ")
print(letterfreq)
print(" ")

# Now the user does his magic
while niz != niz1:
    print("Izberite znak za zamenjavo")
    x = input()
    while x not in obstojeci:
        if x == "restart":
            niz = nizr
            for element in restart1:
                restart1.remove(element)
                restart2.append(element)
            break
        elif x == "izhod":
            raise ImportError
        else:
            pass
        print(" ")
        print("Izbrati morate že obstoječ znak, poskusite še enkrat")
        x = input()
    print(" ")
    print("S čim ga boste zamenjali?")
    if x != "restart":
        y = input()
        while y in obstojeci or y not in male:
            if y == "izhod":
                raise ImportError
            else:
                pass
            print(" ")
            print("Črka je trenutno že uporabljena ali ni ustrezna, poskusite še enkrat")
            y = input()
        niz = niz.replace(x, y)
        obstojeci.remove(x)
        restart1.append(x)
        obstojeci.append(y)
        restart2.remove(y)
    os.system("cls||clear")
    print(niz)
    print(" ")
    print(letterfreq)
    print(" ")
print(" ")
print("Čestitam!")
temp = open("temp.txt", "w+")
raise ImportError
