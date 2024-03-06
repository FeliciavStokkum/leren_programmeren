nummer = 50
totaal = 0
# regel_getal = 0

uitvoer = f"{nummer}"

while totaal < 1000:
    totaal += nummer
    nummer += 1
    uitvoer += f" + {nummer}"
    # regel_getal += 1
    print(f"{nummer - 50}. {uitvoer} = {totaal}") 