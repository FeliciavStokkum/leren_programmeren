# Print alleen het gewicht van de volledige fruitmand.
# Voeg daarna (met code) een watermeloen toe aan de fruitmand en print daarna alleen het gewicht van de volledige fruitmand.
from fruitmand import *

#Functie om het gewicht in de fruitmand te berekenen
def gewicht_fruitmand(): #functie voor het gewicht van de fruitmand te berekenen
    gewicht = 0 #gewicht begint bij 0
    for fruit in fruitmand: 
        gewicht +=  fruit["weight"] #hier het gewicht uit de dictionarie toegevoegd aan de variabele gewicht
    return(gewicht)
print(gewicht_fruitmand()) #hier wordt het gewicht geprint

#Hier voeg ik een watermeloen toe aan de list
watermeloen = {
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}

#Hier hier word de watermeloen toegevoegd aan de fruitmand
fruitmand.append(watermeloen)
print(gewicht_fruitmand())