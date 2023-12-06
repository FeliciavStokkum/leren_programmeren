#schrijf de code om de volgende informatie op te vragen en op te slaan in een dict:
#- automerk
#- model
#- prijs
#- lijst met 5 auto's

#print alleen de 5 prijzen onder elkaar


auto_lijst = []

for i in range(5):
    auto = {}
    auto["merk"] = input("Voer het automerk in: ")
    auto["model"] = input("Voer het model in: ")
    auto["prijs"] = input("Voer een prijs in: ")
    auto_lijst.append(auto)

for auto in auto_lijst:
    print(auto["prijs"])