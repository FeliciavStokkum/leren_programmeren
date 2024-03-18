import random

score = 0
rondes = 0
max_rondes = 20
pogingen_per_ronde = 10

while rondes < max_rondes:
    random_getal = random.randint(1, 1000)
    pogingen_over = pogingen_per_ronde 
    print(f"\nRonde {rondes + 1}. Je hebt {pogingen_over} pogingen over")

    while pogingen_over > 0:
        print(random_getal)
        try:
            poging = int(input(f"Poging {pogingen_per_ronde - pogingen_over + 1}. Voer een getal in om te raden: "))
            pogingen_over -= 1
            verschil = abs(poging - random_getal)

            if poging == random_getal:
                print("Je hebt het geraden! Gefeliciteerd.")
                score += 1
                break  #Beindigd de lus zodra het getal geraden is
            elif verschil <= 20:
                print("Je bent heel warm.")
            elif verschil <= 50:
                print("Je bent warm.")
            elif poging < random_getal:
                print("Hoger")
            elif poging > random_getal:
                print("Lager")
        except ValueError:
            print("Dat is geen geldige invoer, probeer het nog een keer: ")

    rondes += 1
    print(f"\nJe score is: {score}. Je bent nu in ronde: {rondes}.")

    if rondes < max_rondes:
        nieuwe_ronde = input("Nog een ronde spelen? (ja/nee): ")
        if nieuwe_ronde.lower() != "ja":
            print(f"\nTotale score: {score}. Bedankt voor het spelen!")
            break

if rondes == max_rondes:
    print(f"\nJe hebt het maximaal aantal rondes gespeeld. Totale score: {score}. Bedankt voor het spelen!")