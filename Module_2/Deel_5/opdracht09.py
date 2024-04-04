# Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).

from fruitmand import *

for fruit in fruitmand:
    if 'name' == 'druif':
        fruitmand.pop(fruit)
print(fruitmand)