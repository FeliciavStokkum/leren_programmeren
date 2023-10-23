from studieadviestext import *

altijd = 0
vaak = 0 
regelmatig = 0 
soms = 0
nooit = 0

print(STUDIEDOKTER_TITEL)

weken = int(input(AANTAL_WEKEN_VRAAG))

stelling_1 = print(COMPETENTIE_STELLING_1)

antwoord_1 = int(input(OPTIES))

if antwoord_1 == 0:
    altijd += 1
elif antwoord_1 == 1:
    vaak += 1
elif antwoord_1 == 2:
    regelmatig += 1
elif antwoord_1 == 3:
    soms += 1
elif antwoord_1 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

stelling_2 = print(COMPETENTIE_STELLING_2)

antwoord_2 = int(input(OPTIES))

if antwoord_2 == 0:
    altijd += 1
elif antwoord_2 == 1:
    vaak += 1
elif antwoord_2 == 2:
    regelmatig += 1
elif antwoord_2 == 3:
    soms += 1
elif antwoord_2 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

stelling_3 = print(COMPETENTIE_STELLING_3)

antwoord_3 = int(input(OPTIES))

if antwoord_3 == 0:
    altijd += 1
elif antwoord_3 == 1:
    vaak += 1
elif antwoord_3 == 2:
    regelmatig += 1
elif antwoord_3 == 3:
    soms += 1
elif antwoord_3 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

stelling_4 = print(COMPETENTIE_STELLING_4)

antwoord_4 = int(input(OPTIES))

if antwoord_4 == 0:
    altijd += 1
elif antwoord_4 == 1:
    vaak += 1
elif antwoord_4 == 2:
    regelmatig += 1
elif antwoord_4 == 3:
    soms += 1
elif antwoord_4 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

stelling_5 = print(COMPETENTIE_STELLING_5)

antwoord_5 = int(input(OPTIES))

if antwoord_5 == 0:
    altijd += 1
elif antwoord_5 == 1:
    vaak += 1
elif antwoord_5 == 2:
    regelmatig += 1
elif antwoord_5 == 3:
    soms += 1
elif antwoord_5 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

if weken > 10:
 print(COMPETENTIE_STELLING_6)

antwoord_6 = int(input(OPTIES))

if antwoord_6 == 0:
    altijd += 1
elif antwoord_6 == 1:
    vaak += 1
elif antwoord_6 == 2:
    regelmatig += 1
elif antwoord_6 == 3:
    soms += 1
elif antwoord_6 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

if weken > 10:
    print(COMPETENTIE_STELLING_7)

antwoord_7 = int(input(OPTIES))

if antwoord_7 == 0:
    altijd += 1
elif antwoord_7 == 1:
    vaak += 1
elif antwoord_7 == 2:
    regelmatig += 1
elif antwoord_7 == 3:
    soms += 1
elif antwoord_7 == 4:
    nooit += 1
else:
    print(f"Voer een geldig antwoord in: {OPTIES}")

totaal_score = altijd + vaak + regelmatig + soms + nooit

print(COMPETENTIE_ADVIES_TITEL)

if totaal_score <= 2 or totaal_score / 2 <altijd or totaal_score / 2 <vaak:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif totaal_score <= 3 or totaal_score /2 < vaak or totaal_score / 2 < altijd or totaal_score / 2 < regelmatig:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
