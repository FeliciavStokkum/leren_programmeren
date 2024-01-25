nummer = 50
totaal = 0

uitvoer = f"{nummer}"

while totaal < 1000:
    totaal += nummer
    nummer += 1
    uitvoer += f" + {nummer}"
    print(f"{uitvoer} = {totaal}") 