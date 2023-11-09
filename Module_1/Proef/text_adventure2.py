import time
from text_adventure_functies import *

#Initialiseer variabelen
game_over = False
current_location = "Start"


#Main Loop
while not game_over:
    if current_location == "Start":
        verhaal = """Je bevindt je in een rustig dorpje aan de rand van een mysterieus bos,
            \nHet bos staat al eeuwenlang bekend om zijn geheimzinnige krachten en vreemde gebeurtenissen.,
            \nWanneer een dorpeling plotseling verdwijnt, besluit je het bos te betreden om de waarheid te ontdekken.,
            \nTerwijl je het bos verkent, kom je verschillende mysterieuze gebeurtenissen tegen en ontmoet je bewoners van het bos, zoals sprekende dieren, feeën en geesten.,
            \nJe moet aanwijzingen verzamelen om te achterhalen wat er met de verdwenen dorpeling is gebeurd en hoe je hem kunt redden.\nJouw doel is om de verdwenen dorpeling te vinden en het geheim van het bos te ontrafelen,
            \nAfhankelijk van je keuzes en acties, kun je verschillende eindes bereiken."
            \nSucces"""

        print(verhaal)

        current_location = "Begin_bos"

    elif current_location == "Begin_bos":
        print("\nTerwijl je bij de rand van het bos staat, bedenk je wat je moet meenemen op je avontuur. Welke items of uitrusting kies je om je voor te bereiden voordat je het bos betreedt?")
        print("\nJe hebt de volgende opties:")
        print("\n1. een zaklamp")
        print("2. een broodtrommel en een flesje water")
        print("3. Een kompas en een kaart")

        keuze = input("Wat is je keuze?: ")

        if keuze == "1": 
            print("\nWanneer je het bos binnengaat met je zaklamp, merk je meteen een donker pad op dat perkt tot in de diepte van het bos. Wat is je volgende stap?")
            print("\n1: Je neemt een andere route.")
            print("2: je gaat rechtdoor en gebruikt je zaklamp.")
            print("3: je besluit om hier te blijven wachten, tot je zeker weet dat het veilig is.")
            keuze = input("Wat kies je? ")
        if keuze == "2":
            current_location = "welke_richting"
            print("\nMet de broodtrommel en een flesje water in je hand loop je het bos in. \nJe loopt langs prachtig natuur en voordat je het weet bereik je een kruispunt in het bos. \nHet kruispunt heeft 2 paden die je kan betreden.")
            print("\nPad 1: Is verlicht en wanneer je het wat beter bekijkt, zie je dat er verderop een knus huisje zichtbaar is.")
            print("Pad 2: Is donker en loopt wat krom, maar je ziet wel dat dit pad korter is als het eerste pad. Aan het einde zie je een gigantische boom midden op de weg. ")
            keuze = input("Wat kies je? ")
        elif keuze == "3":
            current_location = "Mysterieuze_geluiden"
            print("\nMet je kompas en kaart in de hand, voel je je zeker van je navigatievaardigheden. \nTerwijl je verder het bos in gaat hoor je mysterieuze geluiden, wat doe je om te onderzoeken wat er aan de hand is?")
            print("\nOptie 1: Je gaat het pad onderzoeken, je hebt een kompas en kaart, wat kan er mis gaan?")
            print("Optie 2: Je gaat een andere kant op, je vind het er toch spannend uit zien en durft het niet aan.")
            keuze = input("Wat kies je?")
        else:
            pass
    
    elif current_location == "glinstering":
        keuze = input("Wat is je keuze? ")

        print("Met je kompas en kaart in de hand, voel je je zeker van je navigatievaardigheden. Terwijl je verder het bos in gaat, hoor je mysterieuze geluiden. Wat doe je om te onderzoeken wat er aan de hand is 1: je gaat het pad onderzoeken. 2: je gaat een andere kant op.")

        if keuze == "1":
            pass
        elif keuze == "2":
            pass
        else:
            pass