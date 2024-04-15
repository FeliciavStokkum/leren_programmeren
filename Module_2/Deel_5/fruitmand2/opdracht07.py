# Print alleen de namen van het fruit in de fruitmand die rond zijn, gebruik maximaal 4 regels code (minus lege regels en de import).
from fruitmand import *

# for rond in fruitmand: 
#     if rond["round"]== True: #als round in de fruitmand gelijk is aan True
#         print(rond["name"]) #print de naam van dat fruit

for fruit in fruitmand:
    naam = fruit['name']
    if naam[0] == 'c':
        print(fruit)