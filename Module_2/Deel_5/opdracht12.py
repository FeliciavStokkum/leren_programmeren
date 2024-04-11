# Print de kleur, het gewicht en naam zoals onderstaand voorbeeld (dus volledig Nederlands) van het fruit met de langste naam, je mag alleen de code het juiste stuk fruit laten kiezen.
from fruitmand import *

color_translations = {
    'red': 'rood',
    'green': 'groen',
    'brown': 'bruin',
    'yellow': 'geel',
    'orange': 'oranje',
}

langste_fruitnaam = max(fruitmand, key=lambda x: len(x['name']))

naam = langste_fruitnaam['name']
kleur = color_translations[langste_fruitnaam['color']]
gewicht = langste_fruitnaam['weight']

print(f'De "{naam}" ({len(naam)} letters) heeft een {kleur} kleur en een gewicht van {gewicht / 100} kg')
