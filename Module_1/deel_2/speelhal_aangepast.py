toegangsticket = float(input("Hoeveel kost een toegangsticket? "))
aantal_personen = int(input("Met hoeveel personen ga je? "))
toegangsticket = toegangsticket * 100
toegangs_totaal = aantal_personen * toegangsticket

aantal_minuten_vr = int(input("Hoeveel minuten wil je de gameseat gebruiken? "))
vr_per_5_min = float(input("Hoeveel kost 5 minuten in de gameseat? "))
vr_per_minuut = vr_per_5_min/5
vr_per_minuut = vr_per_minuut * 100
vr_totaal = (vr_per_minuut * aantal_minuten_vr) * aantal_personen

totaal = toegangs_totaal + vr_totaal

print(f"De totale kosten zijn {totaal} euro centen")