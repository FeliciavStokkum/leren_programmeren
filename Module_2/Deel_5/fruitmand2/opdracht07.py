# Print alleen de namen van het fruit in de fruitmand die rond zijn, gebruik maximaal 4 regels code (minus lege regels en de import).
from fruitmand import *

for rond in fruitmand:
    if rond["round"]== True:
        print(rond["name"])