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
PRIJS_SMALL = aantal_small_pizza * SMALL_PIZZA
PRIJS_MEDIUM = aantal_medium_pizza * MEDIUM_PIZZA
PRIJS_LARGE = aantal_large_pizza * LARGE_PIZZA
TOTAAL_PRIJS_PIZZA = (PRIJS_SMALL + PRIJS_MEDIUM + PRIJS_LARGE)

#Totaa; prijs 
bestelde_pizza_small = print(f"Je hebt {aantal_small_pizza} kleine pizza's besteld, dit kost {PRIJS_SMALL}")
bestelde_pizza_medium = print(f"Je hebt {aantal_medium_pizza} medium pizza's besteld, dit kost {PRIJS_MEDIUM}")
bestelde_pizza_large = print(f"Je hebt {aantal_large_pizza} grote pizza's besteld, dit kost {PRIJS_LARGE}")
TOTAAL_PRIJS_PIZZA = print(f"De totaal prijs voor alles pizza's is: {TOTAAL_PRIJS_PIZZA}")

#Bon
print("Hier is uw bon")
print("-----------------------------------------------")
print(f"|  Je hebt totaal {aantal_small_pizza}  kleine pizza's. Dit kost: {PRIJS_SMALL}")
print(f"|  Je hebt totaal {aantal_medium_pizza}  medium pizza's. Dit kost: {PRIJS_MEDIUM}")
print(f"|  Je hebt totaal {aantal_large_pizza}  grote pizza's.  Dit kost: {PRIJS_LARGE}")
print(f"|  Je totaal is                              : {PRIJS_SMALL + PRIJS_MEDIUM + PRIJS_LARGE}")
print("------------------------------------------------")
