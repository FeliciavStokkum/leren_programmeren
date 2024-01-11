from random import choice

kleuren = ("rood", "blauw", "groen", "geel", "bruin")
kleur_koningsdag = "oranje"

aantal_mnm = int(input("Hoeveel m&m wil je toevoegen? "))
kleuren_mnm = []

zak_mnm = {}

for i in range(aantal_mnm):
    kleuren_mnm.append(choice(kleuren))
    kleuren_mnm.append(kleur_koningsdag)

for kleur in kleuren_mnm:
    if kleur in zak_mnm:
        zak_mnm[kleur] += 1
    else:
        zak_mnm[kleur] = 1

print("Dit zijn de kleuren die in de zak zitten: ")
for kleur, aantal in zak_mnm.items():
    print(f"{kleur}: {aantal}")