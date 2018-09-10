# pa se spilajmo malo s slovarji

slovar = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    }

# ker presledkov in vezajev ne stejemo, sem jih izpustil

def prevod(stevilo):
    if stevilo == 1000:
        return "onethousand"
    elif stevilo > 99:
        if stevilo % 100 == 0:
            return slovar[stevilo // 100] + "hundred"
        elif stevilo % 100 < 20 or stevilo % 10 == 0:
            return slovar[stevilo // 100] + "hundredand" + slovar[stevilo % 100]
        else:
            return slovar[stevilo // 100] + "hundredand" + slovar[stevilo % 100 - stevilo % 10] + slovar[stevilo % 10]
    else:
        if stevilo < 20 or stevilo % 10 == 0:
            return slovar[stevilo]
        else:
            return slovar[stevilo - stevilo % 10] + slovar[stevilo % 10]

# stetje crk v prevodih

stevec_crk = 0

for stevilo in range(1, 1001):
    stevec_crk += len(prevod(stevilo))

print(stevec_crk)
