namen = []
naam = input("Voer een naam in: ")


while naam != "stop":
    if naam in namen:
        print("Deze naam zit al in de lijst")
    else:
        namen.append(naam)
    naam = input("Voer een naam in: ")

namen.reverse()
print(namen)