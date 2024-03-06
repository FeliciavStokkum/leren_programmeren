PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
drinken = ("Wat wil je drinken? ")
bandje = ("Heb je een bandje Y/N? ")

#bouw hieronder de floowchart na
leeftijd_input = int(input("Wat is je leeftijd? "))
naam_vraag = "Wat is je naam? "
drinken_vraag = "Wat wil je drinken? "
aantal_jaar_18 = 18 - leeftijd_input
aantal_jaar_21 = 21 - leeftijd_input

if leeftijd_input < 18:
    print(f"Sorry je mag niet naar binnen.Je mag over {aantal_jaar_18} jaar naar binnen.")
elif leeftijd_input > 18:
    naam_input = input(naam_vraag)
    if naam_input in VIP_LIST and leeftijd_input >= 21:
        bandje = "blauw"
        print(f"Je krijgt een {bandje} bandje")
    elif naam_input not in VIP_LIST and leeftijd_input >= 21:
        bandje = "rood"
        print(f"Je krijgt een {bandje} bandje")
