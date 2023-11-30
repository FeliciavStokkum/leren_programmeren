aantal_lijstjes = int(input("Hoeveel lijstjes wil je genereren? "))
lengte_lijstjes = int(input("Hoelang moeten de lijstjes zijn? "))

for i in range(1, aantal_lijstjes + 1):
    huidige_lijst = list(range(i, (i * lengte_lijstjes) + 1, i))
    print(f"lijst {i}: {huidige_lijst}")