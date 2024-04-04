# Print alleen het gewicht van de volledige fruitmand.
# Voeg daarna (met code) een watermeloen toe aan de fruitmand en print daarna alleen het gewicht van de volledige fruitmand.
from fruitmand import *

#Functie om het gewicht in de fruitmand te berekenen
def gewicht_fruitmand():
    gewicht = 0
    for fruit in fruitmand:
        gewicht +=  fruit["weight"]
    return(gewicht)
print(gewicht_fruitmand())

#Hier voeg ik een watermeloen toe aan de list
watermeloen = {
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)
print(gewicht_fruitmand())