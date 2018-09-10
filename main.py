import random
import os

class uporabnik:
    def __init__(self, name, score):
        self.name = name
        self.score = score

integer = "0"

print("Dobrodošli!\n")
print("Že ustvarjeni uporabniški računi:\n")
for file in os.listdir('.'):
    if file[:5]=="user_":
        print("  " + file[5:-4])
print(" ")
print("Med zgoraj navedenimi izberite vaš račun ali napišite želeno uporabniško ime, če ga še nimate.\n")

counter = False
napaka = False

while counter == False:
    napaka = False
    user = input()
    for char in ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]:
        if char in user:
            print("Ime ne sme vsebovati znakov /\\:*?\"<>|. Poskusite še enkrat.")
            napaka = True
    if napaka == False:
        counter = True

name = "user_"+user+".txt"
if os.path.isfile(name):
    upor=open(name, "r")
    parametri = upor.readlines()
    ime = uporabnik(parametri[0][:-1], parametri[1][:-1])
    nov_uporabnik = 0
    
else:
    upor=open(name, "w+")
    upor.write(user+"\n")
    upor.write("0\n")
    upor.close()
    upor=open(name, "r")
    parametri = upor.readlines()
    ime = uporabnik(parametri[0][:-1], parametri[1][:-1])
    nov_uporabnik = 1

# Novemu uporabniku pred začetkom prikaže pravila
os.system("cls||clear")
if nov_uporabnik == 1:
    nov_uporabnik == 0
    try:
        import pravila
    except ImportError:
        pass
    os.system("cls||clear")

while True:
    if os.path.isfile("temp.txt"):
        parametri[1] = str(int(parametri[1][:-1])+1)+"\n"
        upor = open(name, "w+")
        upor.write(parametri[0])
        upor.write(parametri[1])
        upor.close()
        ime.score = parametri[1][:-1]
        os.remove("temp.txt")
    print("Pozdravljeni, "+ime.name+", trenutno imate "+str(ime.score)+" točk. Za nadaljevanje vtipkajte enega izmed naslednjih ukazov:\n")
    print("start - začne z igro")
    print("pravila - odpre pravila igre\n")
    ukaz = input()
    if ukaz == "start":
        os.system("cls||clear")
        try:
            import igra
        except ImportError:
            pass
        os.system("cls||clear")
    elif ukaz == "pravila":
        os.system("cls||clear")
        try:
            import pravila
        except ImportError:
            pass
        os.system("cls||clear")
    else:
        os.system("cls||clear")
