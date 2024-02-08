aantal_lijstjes = int(input("Hoeveel lijstjes wil je genereren? "))

for i in range(1, aantal_lijstjes +1):
    lengte_lijstjes = int(input("Hoelang moet dit lijstje zijn? "))
    huidige_lijst = list(range(i, (i * lengte_lijstjes)))
    print(f"lijst {i}: {huidige_lijst}")

