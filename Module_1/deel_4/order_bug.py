def vraag_getal(volgorde):
    antwoord = input(f"Voer het {volgorde} getal in: ")
    getal = int(antwoord)
    return getal

def deel_getallen(getal_1, getal_2):
    if getal_2 == 0:
        print("Kan niet delen door 0")
        return None
    resultaat = getal_1 / getal_2
    return resultaat

getal_2 = vraag_getal("tweede")
getal_1 = vraag_getal("eerste")

resultaat = deel_getallen(getal_1, getal_2)

if resultaat is not None:
    print("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))
