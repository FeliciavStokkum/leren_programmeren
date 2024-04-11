# Vraag aan de gebruiker om een aantal
# Print het opgegeven aantal keer een random fruitnaam uit de fruitmand. (dus bijv. niet 10 x appel)
from fruitmand import *
import random

aantal = int(input("Voer een aantal in: "))

for i in range(aantal):
    fruit = random.choice(fruitmand)
    print(fruit)