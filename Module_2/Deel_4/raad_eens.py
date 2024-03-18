#To do:
#Na tien keer raden stopt 1 ronde
#Na elke ronde de score melden

import random

score = 0
pogingen = 0
rondes = 0 
max_rondes = 20
max_pogingen = 10

while rondes < max_rondes: #zolang de rondes kleiner zijn als de max_rondes blijft de loop doorgaan
    random_getal = random.randint(1, 1000)
    pogingen_over = max_pogingen - pogingen
    print(f"Ronde {rondes + 1}. Je hebt {pogingen_over} pogingen om het getal te raden.")

    while pogingen_over > 0: #zolang de pogingen_over groter zijn als 0 blijft de loop doorgaan
        print(random_getal)
        print(f"Poging {max_pogingen - pogingen_over + 1}.")
        poging = int(input("Voer een getal in om te raden: "))
        pogingen_over -= 1
        verschil = abs(poging - random_getal)

        if poging == random_getal:
            print("Je hebt het geraden! Gefeliciteerd.")
            score += 1
            break 
        elif verschil <= 20:
            print("Je bent heel warm.")
        elif verschil <= 50:
            print("Je bent warm.")
        elif poging > random_getal:
            print("Lager")
        elif poging < random_getal:
            print("Hoger")
        
    rondes += 1
    print("Je rondes zijn voorbij")
    print(f"Je score is: {score}, je bent in ronde: {rondes}")

    if rondes < max_rondes:
        nieuwe_ronde = input("Nog een ronde spelen? (ja/nee): ")
        if nieuwe_ronde.lower() != "ja":
            print(f"Totale score: {score}. Bedankt voor het spelen!")
            break

if rondes == max_rondes:
    print(f"Je hebt het maximaal aantal rondes gespeeld. Totale score: {score}. Bedankt voor het spelen!")
