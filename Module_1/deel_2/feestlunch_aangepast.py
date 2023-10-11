croissant_prijs = float(input("Hoe duur is een croissant? "))
croissant_prijs = croissant_prijs * 100
stokbrood_prijs = float(input("Hoe duur is een stokbrood? "))
stokbrood_prijs = stokbrood_prijs * 100
croissant_aantal = int(input("Hoeveel croissantjes heb je? "))
stokbrood_aantal = int(input("Hoeveel stokbroodjes heb je? "))
kortingsbonnen_aantal = int(input("Hoeveel kortingsbonnen heb je? "))
waarde_kortingsbonnen = float(input("Hoeveel waarde hebben de kortingsbonnen? "))
waarde_kortingsbonnen = waarde_kortingsbonnen * 100

totaal_croissant = croissant_prijs * croissant_aantal 
totaal_stokbrood = stokbrood_prijs * stokbrood_aantal 
kortingsbonnen = kortingsbonnen_aantal * waarde_kortingsbonnen

totaal = totaal_croissant + totaal_stokbrood - kortingsbonnen
totaal_euro = totaal / 100

afgerond_totaal_euro = round(totaal_euro,2)

print(f"U moet totaal {afgerond_totaal_euro} euro cent betalen.")