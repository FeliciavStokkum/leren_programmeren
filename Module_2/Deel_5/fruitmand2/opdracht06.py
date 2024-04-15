# Print vanuit de fruitmand alleen het gewicht van de appel, gebruik maximaal 4 regels code (minus lege regels en de import).
from fruitmand import *
from random import shuffle
shuffle(fruitmand)

for fruit in fruitmand:
    if fruit['name'] == 'appel':
        print(f"Gewicht van een {fruit['name']}:", fruit['weight']) #hier wordt het gewicht van de appel geprint uit de fruitmand