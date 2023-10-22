rijbewijs = input("Ben je in bezit van een geldig Vrachtwagen rijbewijs? Y/N ").lower()
hoed = input("Ben je in bezig van een hoge hoed? Y/N ").lower()
lichaamsgewicht = int(input("Vul je lichaamsgewicht in hele kg in: "))
lengte = int(input("Vul je lengte in hele centimeters in: "))
certificaat = input("Ben je in het bezit van certificaat: Overleven met gevaarlijk personeel? Y/N ").lower()
dieren_dressur = int(input("Hoeveel jaren praktijkervaring heb je met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaren ervaring heb je met jongleren? "))
acrobatiek = int(input("Hoeveel jaren praktijkervaring heb je met acrobatiek? "))

MAX_WEIGHT = 120
MIN_WEIGHT = 90

MAX_HEIGHT = 220
MIN_HEIGHT = 150

MIN_DIEREN = 4
MIN_JONGLEREN = 5
MIN_ACROBATIEK = 3

if (rijbewijs == "y" and hoed == "y" and certificaat == "y" and lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT and lengte >= MIN_HEIGHT and lengte <= MAX_HEIGHT and dieren_dressur >= MIN_DIEREN and jongleren >= MIN_JONGLEREN and acrobatiek >= MIN_ACROBATIEK):
    print("Gefeliciteerd, u komt in aanmerking voor een sollicitatiegesprek.")
else:
    print("Helaas, je bent niet door de keuring heen.")
