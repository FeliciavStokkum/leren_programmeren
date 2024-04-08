autos = [
    {"merk": "Ferrari", "model": "488 GTB", "motorinhoud": "3.9L V8", "maximale_snelheid": 330},
    {"merk": "Porsche", "model": "911 Turbo S", "motorinhoud": "3.8L flat-6", "maximale_snelheid": 330},
    {"merk": "Lamborghini", "model": "Huracan EVO", "motorinhoud": "5.2L V10", "maximale_snelheid": 325},
    {"merk": "Audi", "model": "RS6 Avant", "motorinhoud": "4.0L V8", "maximale_snelheid": 305},
    {"merk": "BMW", "model": "M5 Competition", "motorinhoud": "4.4L V8", "maximale_snelheid": 305},
    {"merk": "Mercedes-Benz", "model": "AMG GT R", "motorinhoud": "4.0L V8", "maximale_snelheid": 318}
]

total_max_snelheid = 0
teller = 0

for auto in autos:
    teller += 1
    total_max_snelheid += auto['maximale_snelheid']

gemiddelde_max_snelheid = total_max_snelheid / teller
print(gemiddelde_max_snelheid)