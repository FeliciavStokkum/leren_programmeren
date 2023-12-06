aantal_lijstjes = int(input("Hoeveel lijstjes wil je genereren? "))

for i in range(1, aantal_lijstjes +1):
    lengte_lijstjes = int(input("Hoelang moeten de lijstjes zijn? "))
    huidige_lijst = list(range(i, (i * lengte_lijstjes)))
    print(f"lijst {i}: {huidige_lijst}")

#probeer de lengte van de lijstjes aan te passen (3, 4, 5, 3)
#start waarde + lengte