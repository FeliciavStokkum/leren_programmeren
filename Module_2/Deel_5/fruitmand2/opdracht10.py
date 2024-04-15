# Print (met code) de namen en het gewicht in kilogram van het fruit op volgorde van gewicht (zwaarste bovenaan).
from fruitmand import fruitmand

# gesorteerde_fruitmand = sorted(fruitmand, key=lambda x: x['weight'], reverse=True) #hier wordt de fruitmand gesorteerd op gewicht en door de reverste = true word hij van zwaar naar licht gezet.

def sortedFruit(x):
    return x['weight']

gesorteerde_fruitmand = sorted(fruitmand, key=sortedFruit, reverse=True)

for fruit in gesorteerde_fruitmand:
    print(f"{fruit['name']} - {fruit['weight']}g")  #Hier wordt de fruitnaam en gewicht geprint