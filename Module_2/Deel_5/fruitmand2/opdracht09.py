# Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, 
# in maximaal 8 regels code (minus lege regels en de import).
from fruitmand import *

kleuren = []
aantal = 2
for i in range(aantal):
    for fruit in fruitmand:
        if fruit["name"] == "druif" and i == 0: 
            fruitmand.remove(fruit) 
        if fruit['color'] not in kleuren and i == 1:
            kleuren.append(fruit["color"])
print(kleuren)
