import random

namen_lijst = []

while True:
    naam_vraag = input("Voer een naam in: ")

    if naam_vraag not in namen_lijst:
        namen_lijst.append(naam_vraag)
    else:
        print(f"{naam_vraag} staat al in de lijst. Probeer opnieuw.")

    if len(namen_lijst) < 3:
        print("Er moeten minimaal 3 namen worden ingevoerd")
    else:
        while True:
            nieuwe_naam = input("Wil je nog een naam invoeren? ja/nee: ")
            if nieuwe_naam == "ja":
                break
            elif nieuwe_naam == "nee":
                break
            else:
                print("Ongeldige invoer. Gebruik alleen 'ja' of 'nee'. Probeer opnieuw.")
        if nieuwe_naam == "nee":
            break

random.shuffle(namen_lijst)
lootje_dict = {}

for i in range(len(namen_lijst)):
    lootje_dict[namen_lijst[i]] = namen_lijst[(i + 1) % len(namen_lijst)]

uitslag = []

while len(uitslag) < len(namen_lijst):
    welk_lootje = input(f"Van welk lootje wil je de uitslag weten: ")
    if welk_lootje in lootje_dict and welk_lootje not in uitslag:
        print(f"De uitslag van {welk_lootje} is {lootje_dict[welk_lootje]}")
        uitslag.append(welk_lootje)
    elif welk_lootje in uitslag:
        print("Van deze naam weet je de uitslag al.")
    else:
        print("Deze naam zit niet in de lijst.")

print("Alle lootjes zijn nu bekend.")