# Vraag aan de gebruiker om een aantal
# Print het opgegeven aantal keer een random fruitnaam uit de fruitmand. (dus bijv. niet 10 x appel)
from fruitmand import *
import random

aantal = int(input("Voer een aantal in: ")) #Hier vraag ik naar een getal int 

for i in range(aantal):
    while True:
        random_fruit = random.choice(fruitmand)
        if random_fruit['round'] == True:
            print(random_fruit['name'])
            break