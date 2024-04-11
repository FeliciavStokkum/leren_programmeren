# Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, 
# in maximaal 8 regels code (minus lege regels en de import).
from fruitmand import *

for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.remove(fruit)

kleuren = []
for kleur in fruitmand:
    if kleur["color"] not in kleuren:
        kleuren.append(kleur["color"])
print(kleuren)