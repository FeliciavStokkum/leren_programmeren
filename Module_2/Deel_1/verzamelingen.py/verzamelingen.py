tekst = 'Dit is tekst' #string is een verzameling van karakters
tekst_2 = "a" #Dit is ook een verzameling, bestaand uit 1 karakter

for x in range(len(tekst)): #Dit is een manier om net zo vaak code uit te voeren als dat je vooraf wilt weten
    print(tekst[x])

for x in (0, 1, 2, 3):
    print(x)

for x in range(4):
    print(x)

for letter in tekst: #de c verandert per iteratie (herhaling) in het karakter wat dan aan de beurt is. Begint index 0.
    print(letter)

tekst_3 = "Abba was erg populair in de jaren 70"
aantal_keer_a = 0

for c in tekst_3:
    if c == "a":
        aantal_keer_a += 1
print(aantal_keer_a)

for x in range(4):
    print("je bent geweldig")
