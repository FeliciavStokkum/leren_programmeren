from fruitmand import *
# Vraag aan de gebruiker om een kleur uit (alleen) de beschikbare kleuren van de fruitmand, als er toch een kleur gekozen wordt die niet in de fruitmand zit krijgt de gebruiker de melding: “De kleur {kleur} zit er niet in de fruitmand” en wordt de vraag opnieuw gesteld.

kleuren = []
for fruit in fruitmand:
    kleuren.append(fruit["color"])

while True:
    gekozen_kleur = input("Kies een kleur (red/ yellow/ brown/ green/ orange): ").lower()
    if gekozen_kleur in kleuren:
        print(f"{gekozen_kleur} zit in de fruitmand. ")
        break
    else:
        print(f"De kleur {gekozen_kleur} Zit niet in de fruitmand, probeer het opnieuw. ")

# Bepaal het verschil tussen het aantal ronde en niet ronde vruchten van de gekozen kleur.
ronde_vruchten = 0
niet_ronde_vruchten = 0

for fruit in fruitmand:
    if gekozen_kleur == fruit["color"]:
        print(fruit)