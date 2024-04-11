# Print stuk voor stuk de namen van het fruit in de fruitmand in omgekeerde volgorde, gebruik maximaal 3 regels code (minus lege regels en de import).

from fruitmand import *

fruitmand.reverse()
for fruit in fruitmand:
    print(fruit["name"])