# Print stuk voor stuk de namen van het fruit in de fruitmand in omgekeerde volgorde, gebruik maximaal 3 regels code (minus lege regels en de import).

from fruitmand import *

fruitmand.reverse() #hier draai ik de fruitmand om
for fruit in fruitmand[: : -1]: #for loop met elke dictionary in de lijst
    print(fruit["name"]) #hier print ik de fruit namen (deze zijn omgedraaid)

#Twee manieren van omdraaien