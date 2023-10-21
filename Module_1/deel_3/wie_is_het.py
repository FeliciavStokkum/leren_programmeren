#Wie is het? Maar dan met kaas

vraag_1_geel = input("Is de kaas geel? ")
if vraag_1_geel == "ja":
    vraag_2_gaten = input("Zitten er gaten in? ")
    if vraag_2_gaten == "ja":
        vraag_3_duur = input("Is de kaas belachelijk duur? ")
        if vraag_3_duur == "ja":
            print("Emmenthaler")
        elif vraag_3_duur == "nee":
            print("Leerdammer")
    elif vraag_2_gaten == "nee":
         vraag_4_hard = input("Is de kaas hard als steen? ")
         if vraag_4_hard == "ja":
             print("Parmigiano Reggiano")
         elif vraag_4_hard == "nee":
              print("Goudse kaas")
elif vraag_1_geel == "nee":
    vraag_5_schimmel = input("Heeft de kaas blauwe schimmel? ")
    if vraag_5_schimmel == "ja":
        vraag_6_korst = input("Heeft de kaas een korst? ")
        if vraag_6_korst == "ja":
            print("Bleu de Rochbaron")
        elif vraag_6_korst == "nee":
                print("Foume d'ambert")
    elif vraag_5_schimmel == "nee":
        vraag_7_korst = input("Heeft de kaas een korst? ")
        if vraag_7_korst == "ja":
                print("Camembert")
        else: 
                print("Mozzarella")