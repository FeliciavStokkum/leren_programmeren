#Felicia van Stokkum 
#Opdracht Pizza Calculator

#Prijzen van de pizza's
while True:
    try:
        small_pizza = float(input("Hoeveel kost een kleine pizza? "))
        break
    except ValueError:
        print("Ongeldigde invoer, hoeveel een kleine pizza? ")

while True:
    try:
        medium_pizza = float(input("Hoeveel kost een medium pizza? "))
        break
    except ValueError:
        print("Ongeldige invoer, hoeveel kost een medium pizza? ")

while True:
    try:
        large_pizza = float(input("Hoeveel kost een groote pizza? "))
        break
    except ValueError:
        print("Ongeldige invoer, hoeveel kost een groote pizza? ")

#Input van de aantallen voor de pizza's 
while True:
    try:
        aantal_small_pizza = int(input("Hoeveel kleine pizza's wil je? "))
        break
    except ValueError:
        print("Ongeldige invoer, hoeveel kleine pizza's wil je? ")

while True:
    try:
        aantal_medium_pizza = int(input("Hoeveel medium pizza's wil je? "))
        break
    except ValueError:
        print("Ongeldige invoer, hoeveel medium pizza's wil je? ")

while True:
    try:
        aantal_large_pizza = int(input("Hoeveel large pizza's wil je? "))
        break
    except ValueError:
        print("Ongeldige invoer, hoeveel groote pizza's wil je? ")

#prijzen voor de pizza's
prijs_small = aantal_small_pizza * small_pizza
prijs_medium = aantal_medium_pizza * medium_pizza
prijs_large = aantal_large_pizza * large_pizza
totaal_prijs_pizza = (prijs_small + prijs_medium + prijs_large)

#Totaa; prijs 
bestelde_pizza_small = print(f"Je hebt {aantal_small_pizza} kleine pizza's besteld, dit kost {prijs_small}")
bestelde_pizza_medium = print(f"Je hebt {aantal_medium_pizza} medium pizza's besteld, dit kost {prijs_medium}")
bestelde_pizza_large = print(f"Je hebt {aantal_large_pizza} grote pizza's besteld, dit kost {prijs_large}")
totaal_prijs_pizza = print(f"De totaal prijs voor alles pizza's is: {totaal_prijs_pizza}")

#Bon
print("Hier is uw bon")
print("-----------------------------------------------")
print(f"|  Je hebt totaal {aantal_small_pizza}  kleine pizza's. Dit kost: {prijs_small}")
print(f"|  Je hebt totaal {aantal_medium_pizza}  medium pizza's. Dit kost: {prijs_medium}")
print(f"|  Je hebt totaal {aantal_large_pizza}  grote pizza's.  Dit kost: {prijs_large}")
print(f"|  Je totaal is                              : {prijs_small + prijs_medium + prijs_large}")
print("------------------------------------------------")
