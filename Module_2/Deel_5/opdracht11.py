from fruitmand import *
# Vraag aan de gebruiker om een kleur uit (alleen) de beschikbare kleuren van de fruitmand, als er toch een kleur gekozen wordt die niet in de fruitmand zit krijgt de gebruiker de melding: “De kleur {kleur} zit er niet in de fruitmand” en wordt de vraag opnieuw gesteld.

kleuren = []
for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit["color"])
print(kleuren)

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

# for fruit in fruitmand:
#     if gekozen_kleur == fruit['color'] and fruit['round'] == True: 
#         ronde_vruchten += 1
#     elif gekozen_kleur == fruit['color'] and fruit['round'] == False:
#         niet_ronde_vruchten += 1

for fruit in fruitmand:
    if gekozen_kleur == fruit['color']:
        if fruit['round'] == True: 
            ronde_vruchten += 1
        else:
            niet_ronde_vruchten += 1


verschil = ronde_vruchten - niet_ronde_vruchten

# Print vervolgens het volgende als er van de gekozen kleur het verschil van de vrucht:
if verschil > 0:
    print(f"Er zijn {abs(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif verschil < 0:
    print(f"Er zijn {abs(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif verschil == 0:
    print(f"Er zijn {ronde_vruchten} ronde vruchten en {niet_ronde_vruchten} niet ronde vruchten in de kleur {gekozen_kleur}")