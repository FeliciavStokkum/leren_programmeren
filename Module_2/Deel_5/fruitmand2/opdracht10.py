# Print (met code) de namen en het gewicht in kilogram van het fruit op volgorde van gewicht (zwaarste bovenaan).
from fruitmand import fruitmand

gesorteerde_fruitmand = sorted(fruitmand, key=lambda x: x['weight'], reverse=True)

for fruit in gesorteerde_fruitmand:
    print(f"{fruit['name']} - {fruit['weight']}g")