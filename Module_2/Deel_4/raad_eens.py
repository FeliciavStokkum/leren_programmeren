#To do:
#Zorgen dat er na elke ronde/ goed geraden nummer word gevraagd of ze nog een ronde willen, tenzij er al 20 rondes zijn geweest
#Als het absolute getal kleiner is als 20, print: "Je bent heel warm"
#Als het absolute getal kleiner is als 50, print: "Je bent warm"
#Elk gerade getal is 1 ronde
#Na tien keer raden stopt 1 ronde
#Na elke ronde de score melden
#Aan het einde de eindscore melden
#Pogingen na goed geraden moeten veranderen

import random

score = 0
pogingen = 0
rondes = 0 

while rondes < 20:
    random_getal = random.randint(1, 1000)
    while pogingen < 10:
        print(random_getal)
        poging = int(input("Voer een getal in om te raden: "))
        pogingen += 1
        print(f"poging nummer {pogingen}")
        if poging == random_getal:
            print("Je hebt het geraden! Gefeliciteerd")
            score += 1
            rondes += 1 
            print(f"Je score is: {score}")
            nieuwe_ronde = input("Nog een ronde spelen? (ja/nee): ")
            if nieuwe_ronde.lower() != "ja":
                print(f"Totale score: {score} geraden in {pogingen} pogingen.")
                exit()
            else:
                break
        if abs(poging) < 20:
            print("Je bent heel warm")
        elif abs(poging) < 50:
            print("Je bent warm")
        elif poging < random_getal:
            print("Hoger")
        elif poging > random_getal:
            print("Lager")

print(f"Je hebt het maximaal aantal rondes gespeeld. Totale score: {score} geraden in {pogingen} pogingen.")