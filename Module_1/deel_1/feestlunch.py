# Je wilt 17 croissantjes van elk 39 eurocent en 2 stokbroden van elk 2,78 euro kopen. 
# Je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen?

croissant = 0.39
stokbrood = 2.78

totaal_croissant = croissant * 17
totaal_stokbrood = stokbrood * 2
kortingsbonnen = 3 * 0.50

totaal = totaal_croissant + totaal_stokbrood - kortingsbonnen

print(totaal)
