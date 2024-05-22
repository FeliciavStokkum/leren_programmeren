import random

namen_lijst = []

while True:
    i_vraag = input("Voer een naam in: ")

    if i_vraag not in namen_lijst:
        namen_lijst.append(i_vraag)
        print(f"i toegevoegd. Huidige namenlijst: {namen_lijst} \n")
    else:
        print("i staat al in de lijst. Probeer opnieuw.")

    if len(namen_lijst) < 3: 
        print("\n")
    else:
        while True:
            nieuwe_i = input("Wil je nog een naam invoeren? ja/nee: ")
            if nieuwe_i == "ja":
                break
            elif nieuwe_i == "nee":
                break
            else:
                print("Ongeldige invoer. Gebruik alleen 'ja' of 'nee'. Probeer opnieuw. \n")
        if nieuwe_i == "nee":
            break

random.shuffle(namen_lijst)

print("De lootjes zijn:")
for i in range(len(namen_lijst)):
    print(f"{namen_lijst[i]} heeft {namen_lijst[(i + 1) % len(namen_lijst)]}. ")