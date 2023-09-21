vr_factor = int(input("Hoeveel minuten wil je in de VR? "))
hoeveel_mensen = int(input("Met hoeveel mensen wil je gaan? "))
toegang_prijs = int(input("Hoeveel centen kost de toegangsticket? "))

toegang_prijs_centen= int(toegang_prijs * 100)

vr_factor_prijs_per_minuut = vr_factor / 5 * 0.37 * 100

totaal_prijs_vr_centen = vr_factor_prijs_per_minuut * hoeveel_mensen

totaal_prijs_toegang_centen = toegang_prijs_centen * hoeveel_mensen

totaal_centen = totaal_prijs_toegang_centen + totaal_prijs_vr_centen

totaal_euro = totaal_centen / 100

print(f"Je moet in totaal {totaal_euro:.2f} euro betalen.")