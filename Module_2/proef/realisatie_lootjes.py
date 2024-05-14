lijst_namen = []

hoeveel_namen = input("Hoeveel namen wil je invoeren?: ")

namen = input("Voer een naam in: ")

while True:
    if namen not in lijst_namen:
        lijst_namen.append(namen)
        print(lijst_namen)
    else:
        print("Naam zit al in de lijst, probeer opnieuw: ")

    while True: 
        meer_namen = input("Wil je meer namen toevoegen? ja/nee: ")
        if meer_namen == 'ja':
            namen = input("Voer een naam in: ")
            lijst_namen.append(namen)
            print(lijst_namen)
        else:
            print("Je wilt niet meer namen toevoegen. ")
            print(lijst_namen)
            break
        