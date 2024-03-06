boodschappenlijstje = {}

while True:
    artikel = input("Welk artikel wilt u toevoegen? ")
    hoeveel = int(input(f"Hoeveel {artikel} wilt u toevoegen? "))

    if artikel.lower() in boodschappenlijstje:
        boodschappenlijstje[artikel.lower()] += hoeveel 
    else:
        boodschappenlijstje[artikel.lower()] = hoeveel

    print(f"{artikel} is toegevoegd aan uw boodschappenlijstje")
    toevoegen = input("Wilt u nog meer artikelen toevoegen? ")
    if toevoegen.lower() == "nee":
        break

print("")
print("--UW BOODSCHAPPENLIJSTJE--")
print("")
for artikel, hoeveel in boodschappenlijstje.items():
    print(f"{hoeveel}x {artikel}")
print("__________________________")