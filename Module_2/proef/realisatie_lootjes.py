import random 
namen_lijst = []

nieuwe_naam = ("Wil je nog een naam invoeren? ja/nee: ")

while True:
    lengte_namen_lijst = len(namen_lijst) + 1
    naam_vraag = input("Voer een naam in: ")

    if naam_vraag not in namen_lijst:
        namen_lijst.append(naam_vraag)
        print(f"Naam toegevoegd. Huidige namenlijst: {namen_lijst}")
    else:
        print("Naam staat al in de lijst. Probeer opnieuw.")
        continue

    if lengte_namen_lijst < 3: 
        print(naam_vraag)
    elif lengte_namen_lijst >= 3:
        print(input(nieuwe_naam))
        
        if nieuwe_naam != "ja":
            break
        else:
            print("Ongeldige invoer. type 'ja' of 'nee'")
            print(input(nieuwe_naam))

#Hier word de lijst met namen geprint en het aantal dat in de lijst zit
print(f"Eindlijst met namen: {namen_lijst}, er staan {lengte_namen_lijst} namen in de lijst")

#Namen (lootjes) worden geschut
random.shuffle(namen_lijst)