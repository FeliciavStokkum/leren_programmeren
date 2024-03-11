PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

drinken = "Wat wil je drinken? "
bandje = ""
complimenten = "Alstublieft, complimenten van het huis"
leeftijd_input = int(input("Wat is je leeftijd? "))
naam_vraag = "Wat is je naam? "
drinken_vraag = "Wat wil je drinken? "
aantal_jaar_21 = 21 - leeftijd_input
aantal_jaar_18 = 18 - leeftijd_input

if leeftijd_input < 18:
    print(f"Sorry je mag niet naar binnen. Probeer het in {aantal_jaar_18} jaar nog eens.")
else:  
    naam_input = input(naam_vraag)
    if naam_input.lower() in VIP_LIST: 
        if leeftijd_input >= 21:
            bandje = "blauw"
        else:
            bandje = "rood"
        print(f"Je krijgt een {bandje} bandje")
    else:
        if leeftijd_input >= 21:
            stempel = True
            print("Je krijgt een stempel.")
    
    drinken_input = input(drinken_vraag).lower() 
    if drinken_input in DRANKJES:
        if drinken_input == "cola":
            if bandje:
                print(complimenten)
            else:
                print(f"Alsjeblieft je cola, dat is dan €{PRIJS_COLA}.")

        elif drinken_input == "bier":
            if bandje == "blauw" or bandje == "rood":
                print(complimenten)
            else:
                if leeftijd_input < 21:
                    aantal_jaar_21 = 21 - leeftijd_input
                    print(f"Sorry geen alcohol voor jou. Kom over {aantal_jaar_21} jaar terug")
                elif stempel:
                    print(f"Alsjeblieft je {DRANKJES[1]}. Dat is dan €{PRIJS_BIER}.")
        
        elif drinken_input == "champagne":
            if leeftijd_input < 21:
                print(f"Sorry geen alcohol voor jou. Kom over {aantal_jaar_21} jaar terug")
            else:
                if bandje == "blauw":
                    print(f"Alsjeblieft je champagne. Dat is dan €{PRIJS_CHAMPAGNE}.")
                else:
                    print("Sorry, alleen vips mogen champagne bestellen.")
    else:
        print("Sorry geen idee wat je bedoeld, hier een glaasje water. ")