import time

def introductie():
    print("Welkom in het text adventure spel!")
    naam = input("Wat is je naam? ")
    print(f"Hallo, {naam}! Laten we beginnen.")
    time.sleep(1)

def verhaal():
    print("\nJe wordt wakker in een mysterieus bos.")
    time.sleep(1)
    print("Je hebt geen idee hoe je hier terecht bent gekomen.")
    time.sleep(1)
    print("Je hebt de volgende opties:")
    time.sleep(1)
    print("1. Volg het verlichte pad.")
    print("2. Doorzoek de omgeving op aanwijzingen.")
    print("3. Roep om hulp.")

    keuze = input("Wat ga je doen? (1/2/3): ")

    if keuze == "1":
        volg_het_pad()
    elif keuze == "2":
        doorzoek_de_omgeving()
    elif keuze == "3":
        roep_om_hulp()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        verhaal()

def volg_het_pad():
    print("\nJe volgt het verlichte pad en komt aan bij een betoverende vijver.")
    time.sleep(1)
    print("In de vijver zie je je eigen spiegelbeeld.")
    time.sleep(1)
    print("Je hebt twee opties:")
    time.sleep(1)
    print("1. Drink het water uit de vijver.")
    print("2. Ga verder langs het pad zonder het water aan te raken.")

    keuze = input("Wat ga je doen? (1/2): ")

    if keuze == "1":
        drink_het_water()
    elif keuze == "2":
        ga_verder_langs_het_pad()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        volg_het_pad()

def drink_het_water():
    print("\nJe drinkt het water uit de vijver en voelt een golf van kracht over je heen komen.")
    time.sleep(1)
    print("Je kunt nu communiceren met dieren en begrijpt de taal van het bos.")
    time.sleep(1)
    print("Gefeliciteerd, je hebt nieuwe krachten verworven!")

def ga_verder_langs_het_pad():
    print("\nJe vervolgt je weg langs het pad en komt aan bij een brug over een kolkende rivier.")
    time.sleep(1)
    print("De brug ziet er oud en gammel uit.")
    time.sleep(1)
    print("Je hebt twee opties:")
    time.sleep(1)
    print("1. Steek de brug over.")
    print("2. Zoek een andere route om de rivier over te steken.")

    keuze = input("Wat ga je doen? (1/2): ")

    if keuze == "1":
        steek_de_brug_over()
    elif keuze == "2":
        zoek_een_andere_route()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        ga_verder_langs_het_pad()

def steek_de_brug_over():
    print("\nJe steekt de brug over, maar halverwege begint deze te kraken.")
    time.sleep(1)
    print("Je valt in de rivier en wordt meegesleurd door de stroming.")
    time.sleep(1)
    print("Helaas, je hebt gefaald. Probeer opnieuw.")

def zoek_een_andere_route():
    print("\nJe zoekt een andere route en vindt een smalle boomstam die de rivier overspant.")
    time.sleep(1)
    print("Je balanceert voorzichtig over de boomstam en bereikt veilig de overkant.")
    time.sleep(1)
    print("Gefeliciteerd, je hebt de rivier overgestoken!")

def doorzoek_de_omgeving():
    print("\nJe doorzoekt de omgeving en vindt een oude kaart in een boomstronk.")
    time.sleep(1)
    print("De kaart toont een verborgen schat ergens in het bos.")
    time.sleep(1)
    print("Je hebt twee opties:")
    time.sleep(1)
    print("1. Volg de kaart naar de verborgen schat.")
    print("2. Ga verder langs het verlichte pad.")

    keuze = input("Wat ga je doen? (1/2): ")

    if keuze == "1":
        volg_de_kaart()
    elif keuze == "2":
        ga_verder_langs_het_pad()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        doorzoek_de_omgeving()

def volg_de_kaart():
    print("\nJe volgt de kaart en komt aan bij een verborgen grot.")
    time.sleep(1)
    print("In de grot vind je een kostbare schat en keert terug als een rijke avonturier!")
    time.sleep(1)
    print("Gefeliciteerd, je hebt het spel gewonnen!")

def roep_om_hulp():
    print("\nJe roept om hulp, maar niemand lijkt je te horen.")
    time.sleep(1)
    print("Je besluit verder te gaan met je zoektocht.")
    time.sleep(1)
    ga_verder_langs_het_pad()

if __name__ == "__main__":
    introductie()
    verhaal()
