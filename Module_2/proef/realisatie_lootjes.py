import random

namen_lijst = []

while True:
    naam_vraag = input("Voer een naam in: ")

    if naam_vraag not in namen_lijst:
        namen_lijst.append(naam_vraag)
        print(f"Naam toegevoegd. Huidige namenlijst: {namen_lijst} \n")
    else:
        print("Naam staat al in de lijst. Probeer opnieuw.")

    if len(namen_lijst) < 3: 
        print("\n")
    else:
        while True:
            nieuwe_naam = input("Wil je nog een naam invoeren? ja/nee: ")
            if nieuwe_naam == "ja":
                break
            elif nieuwe_naam == "nee":
                break
            else:
                print("Ongeldige invoer. Gebruik alleen 'ja' of 'nee'. Probeer opnieuw. \n")
        if nieuwe_naam == "nee":
            break

# Hier wordt de lijst met namen geprint en het aantal dat in de lijst zit
print(f"Eindlijst met namen: {namen_lijst}, er staan {len(namen_lijst)} namen in de lijst \n")

# Namen (lootjes) worden geschud
# random.shuffle(namen_lijst)
# print(f"De namen zijn geschud: {namen_lijst}")

# for naam in range(len(namen_lijst)):
#     lootje_een = namen_lijst[naam]
#     lootje_twee = namen_lijst[(naam + 1)]
#     print(f"{lootje_een} heeft {lootje_twee}")

#Random naam uit lijst halen
#Controleren of gelijk is aan eerste naam
#Niet gelijk print lootjes
#Item dat hetzelfde was verwijderen

for naam in namen_lijst:
    lootje = random.choice(namen_lijst)
    while lootje == naam:
        lootje = random.choice(namen_lijst)
    print(f"{naam} heeft {lootje}")