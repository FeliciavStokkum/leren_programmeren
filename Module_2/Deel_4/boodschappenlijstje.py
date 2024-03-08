boodschappenlijstje = {}

while True:
    artikel = input("Welk artikel wilt u toevoegen? ").lower()
    hoeveel = int(input(f"Hoeveel {artikel} wilt u toevoegen? "))

    if artikel in boodschappenlijstje:
        boodschappenlijstje[artikel] += hoeveel 
    else:
        boodschappenlijstje[artikel] = hoeveel

    print(f"{artikel} is toegevoegd aan uw boodschappenlijstje")
    toevoegen = input("Wilt u nog meer artikelen toevoegen? ").lower()
    if toevoegen == "nee":
        break

print("")
print("--UW BOODSCHAPPENLIJSTJE--")
print("")
for artikel, hoeveel in boodschappenlijstje.items():
    print(f"{hoeveel}x {artikel}")
print("__________________________")