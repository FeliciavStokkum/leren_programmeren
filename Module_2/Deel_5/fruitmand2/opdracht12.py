# Print de kleur, het gewicht en naam zoals onderstaand voorbeeld (dus volledig Nederlands) van het fruit met de langste naam, je mag alleen de code het juiste stuk fruit laten kiezen.
from fruitmand import *

#Alle kleuren in de fruitmand
color_translations = {
    'red': 'rood',
    'green': 'groen',
    'brown': 'bruin',
    'yellow': 'geel',
    'orange': 'oranje',
    'purple' : 'paars', 
    'pink' : 'roze', 
    'black' : 'zwart',
}

def lengteFruit(pietje):
    return len(pietje['name'])
    # return lengte = len(fruit['name'])
    # return lengte

# langste_fruitnaam = max(fruitmand, key=lambda x: len(x['name'])) #Hier wordt de lengte van de namen berekend

langste_fruitnaam = max(fruitmand, key=lengteFruit)

naam = langste_fruitnaam['name']
kleur = color_translations[langste_fruitnaam['color']]
gewicht = langste_fruitnaam['weight']

print(f'De "{langste_fruitnaam["name"]}" ({len(naam)} letters) heeft een {kleur} kleur en een gewicht van {gewicht / 100} kg')
print(langste_fruitnaam)