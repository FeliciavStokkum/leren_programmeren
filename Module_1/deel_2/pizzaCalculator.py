#Felicia van Stokkum 
#Opdracht Pizza Calculator

#Prijzen van de pizza's
SMALL_PIZZA = 6.99
MEDIUM_PIZZA = 8.49
LARGE_PIZZA = 11.99

#Input van de aantallen voor de pizza's 
aantal_small_pizza = int(input("Hoeveel kleine pizza's wil je? "))
aantal_medium_pizza = int(input("Hoeveel medium pizza's wil je? "))
aantal_large_pizza = int(input("Hoeveel large pizza's wil je? "))

#prijzen voor de pizza's
prijs_small = aantal_small_pizza * SMALL_PIZZA
prijs_medium = aantal_medium_pizza * MEDIUM_PIZZA
prijs_large = aantal_large_pizza * LARGE_PIZZA
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
