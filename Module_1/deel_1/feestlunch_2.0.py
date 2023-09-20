croissant_prijs = 0.39
stokbrood_prijs = 2.78
croissant_aantal = 17
stokbrood_aantal = 2

totaal_croissant = croissant_prijs * 17
totaal_stokbrood = stokbrood_prijs * 2
kortingsbonnen = 3 * 0.50

totaal = totaal_croissant + totaal_stokbrood - kortingsbonnen

print(f"De feestlunch kost je bij de bakker {totaal} euro voor de {croissant_aantal} croissantjes en de {stokbrood_aantal} stokbroden als de {kortingsbonnen_aantal} kortingsbonnen nog geldig zijn!")