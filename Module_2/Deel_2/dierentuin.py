from random import shuffle, choice
import time

DIEREN = ["Giraffe", "Zebra", "Struisvogel", "Gazelle", "Emoe"]
dieren_lijst = []
dieren_teller = {}

for _ in range(75):
    dieren_lijst.append(choice(DIEREN))

for _ in range(3):
    dieren_lijst.append("Neushoorn")

for dier in dieren_lijst:
    if dier in dieren_teller:
        dieren_teller[dier] += 1
    else: 
        dieren_teller[dier] = 1

#for dier in dieren_teller.keys(): #alleen de keys
#for aantal in dieren_teller.values(): #alleen de values
for dier, aantal in dieren_teller.items():
    if input(f"Er zijn {aantal} {dier}, klopt dit? (ja/nee)") == "nee":
        print(f"Tel dan nu zelf de {dier}")
        dieren_teller[dier] = int(input("en hoeveel heb je er?"))

totaal = 0

print("Rapport Savanne:")
for dier, aantal in dieren_teller.items():
    print(f"{dier}: {aantal}")
    totaal += aantal
print(f"totaal: {totaal}")