import random
#Toevoegen nieuwe ronde meerdere input

score = 0
rondes = 0
MAX_RONDES = 20
POGINGEN_PER_RONDE = 10

while rondes < MAX_RONDES:
    random_getal = random.randint(1, 1000)
    pogingen_over = POGINGEN_PER_RONDE 
    print(f"\nRonde {rondes + 1}. Je hebt {pogingen_over} pogingen over")

    while pogingen_over > 0:
        print(random_getal)
        try:
            poging = int(input(f"Poging {POGINGEN_PER_RONDE - pogingen_over + 1}. Voer een getal in om te raden: "))
            pogingen_over -= 1
            verschil = abs(poging - random_getal)

            if poging == random_getal:
                print("Je hebt het geraden! Gefeliciteerd.")
                score += 1
                break  
            if verschil <= 20:
                print("Je bent heel warm.")
            elif verschil <= 50:
                print("Je bent warm.")
            if poging < random_getal:
                print("Hoger")
            elif poging > random_getal:
                print("Lager")
        except ValueError:
            print("Dat is geen geldige invoer, probeer het nog een keer: ")

    rondes += 1
    print(f"\nJe score is: {score}. Je bent nu in ronde: {rondes}.")

    if rondes < MAX_RONDES:
        print("Nog een ronde spelen? ")
    while True:
        vraag = input("(ja/ nee): ").lower()
        if vraag in ['ja', 'nee']:
            break
        else:
            print("Antwoord alleen met 'ja' of 'nee'.")
    if vraag == 'nee':
        break

print(f"Je bent gestopt, je score is nu {score} ")

if rondes == MAX_RONDES:
    print(f"\nJe hebt het maximaal aantal rondes gespeeld. Totale score: {score}. Bedankt voor het spelen!")
    