rijbewijs = input("Ben je in bezit van een geldig Vrachtwagen rijbewijs? Y/N ").lower()
hoed = input("Ben je in bezig van een hoge hoed? Y/N ").lower()
lichaamsgewicht = int(input("Vul je lichaamsgewicht in hele kg in: "))
lengte = int(input("Vul je lengte in hele centimeters in: "))
certificaat = input("Ben je in het bezit van certificaat: Overleven met gevaarlijk personeel? Y/N ").lower()
dieren_dressur = int(input("Hoeveel jaren praktijkervaring heb je met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaren ervaring heb je met jongleren? "))
acrobatiek = int(input("Hoeveel jaren praktijkervaring heb je met acrobatiek? "))
mbo_4 = input("Ben je in het bezit van een MBO-4 diploma ondernemen? Y/N ").lower()
ondernemer = int(input("Hoelang ben u een ondernemer, vul in hele jaren in: "))
werknemer = int(input("Hoeveel werknemers heeft u? "))

man = input("bent u een man? Y/N")
if man == "Y":
    snor = int(input("Hoe breed is uw snor? Vul in hele getallen in: "))
else:
    snor = ""

vrouw = input("Bent u een vrouw? Y/N ")
if vrouw == "Y":
    haar_kleur = input("Wat is uw haarkleur? ")
    haar_lengte = input("Hoelang is uw haar? ")
else:
    haar_kleur = ""
    haar_lengte = 0

anders = input("Is uw gender niet man of vrouw? Y/N ")
if anders == "Y":
    glimlach = int(input("Hoe breed is uw glimlach? "))

MAX_WEIGHT = 120
MIN_WEIGHT = 90

MAX_HEIGHT = 220
MIN_HEIGHT = 150

MIN_DIEREN = 4
MIN_JONGLEREN = 5
MIN_ACROBATIEK = 3

MIN_ONDERNEMER = 3
MIN_WERKNEMERS = 5

SNOR_BREED = 10
GLIMLACH = 10

rijbewijs_ok = rijbewijs == "y"
hoed_ok = hoed == "y"
lichaamsgewicht_ok = lichaamsgewicht >= MIN_WEIGHT
lengte_ok = lengte >= MIN_HEIGHT
certificaat_ok = certificaat == "y"
dieren_dressur_ok = dieren_dressur >= MIN_DIEREN
jongleren_ok = jongleren >= MIN_JONGLEREN
acrobatiek_ok = acrobatiek >= MIN_ACROBATIEK
mbo_4_ok = mbo_4 == "y"
ondernemer_ok = ondernemer >= MIN_ONDERNEMER
werknemer_ok = werknemer >= MIN_WERKNEMERS
man_ok = man == "y"
snor_ok = snor >= SNOR_BREED
vrouw_ok = vrouw == "y"
haar_kleur_ok = haar_kleur == "rood"
haar_lengte_ok = haar_lengte >= 20
anders_ok = anders == "y"
glimlach_ok = glimlach >= GLIMLACH


if (rijbewijs_ok and hoed_ok and lichaamsgewicht_ok and certificaat_ok) and (mbo_4_ok or ondernemer_ok and werknemer_ok) and (man_ok and snor_ok) or (vrouw_ok and haar_kleur_ok and haar_lengte_ok) or (anders_ok and glimlach_ok) and (dieren_dressur_ok or jongleren_ok or acrobatiek_ok): 
#rijbewijs_ok and hoed_ok and certificaat_ok and lichaamsgewicht_ok and lengte_ok and
#     dieren_dressur_ok and jongleren_ok and acrobatiek_ok and
#     mbo_4_ok and ondernemer_ok and werknemer_ok and
#     snor_ok and haar_kleur_ok and haar_lengte_ok and glimlach_ok:
    print("Gefeliciteerd, u komt in aanmerking voor een sollicitatiegesprek.")
else:
    if not rijbewijs_ok:
        print("U heeft geen geldig rijbewijs")
    if not hoed_ok:
        print("U heeft geen hoge hoed")
    if not lichaamsgewicht_ok:
        print("U voldoet niet aan onze gewicht eisen")
    if not lengte_ok:
        print("U voldoet niet aan onze lengte eisen")
    if not certificaat_ok:
        print("U heeft geen certificaat; overleven met gevaarlijk personeel")
    if not dieren_dressur_ok:
        print("U heeft niet genoeg ervaring in dieren-dressuur")
    if not jongleren_ok:
        print("U heeft niet genoeg ervaring in jongleren")
    if not acrobatiek_ok:
        print("U heeft genoeg ervaring in acrobatiek")
    if not mbo_4_ok:
        print("U heeft geen diploma mbo-4 ondernemen")
    if not ondernemer_ok:
        print("U bent niet lang genoeg werknemer")
    if not werknemer_ok:
        print("U heeft te weinig werknemers")
    if not snor_ok:
        print("Uw snor is niet breed genoeg")
    if not haar_kleur_ok:
        print("U heeft niet de juiste haarkleur")
    if not haar_lengte_ok:
        print("U heeft niet de juiste haar lengte")
    if not glimlach_ok:
        print("Uw glimlach is niet breed genoeg")