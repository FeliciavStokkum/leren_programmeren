vr_factor = float(input("Hoeveel minuten wil je in de VR? "))
hoeveel_mensen = int(input("Met hoeveel mensen wil je gaan? "))
toegang_prijs = float(input("Hoe duur is de toegangs prijs? "))

vr_factor_prijs = vr_factor / 5 * 0.37
totaal_prijs_vr = vr_factor_prijs * hoeveel_mensen

totaal_prijs_toegang = toegang_prijs * hoeveel_mensen

totaal = totaal_prijs_toegang + totaal_prijs_vr

print(totaal)

print(f"Je moet totaal {totaal} betalen.")