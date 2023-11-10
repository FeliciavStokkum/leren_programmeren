import time
from text_adventure_functies2 import *

# Initialiseer variabelen
game_over = False
current_location = "Start"

# Luistert aandachtig

# Main Loop
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
        begin_bos()

        keuze = input("Wat is je keuze?: ")
        if keuze == "1":
            print("Je hebt gekozen voor een zaklamp")
            current_location = "Donkere_pad"

        elif keuze == "2":
            print("Je hebt gekozen voor een broodtrommel en een flesje water")
            current_location = "welke_richting"

        elif keuze == "3":
            print("Een kompas en een kaart")
            current_location = "Mysterieuze_geluiden"
        else:
            print("Ongeldige invoer, probeer opnieuw.")

    elif current_location == "Donkere_pad":
        donkere_pad()
        keuze = input("Wat kies je? ")
        if keuze == "1":
            print("Je hebt gekozen voor een andere route")
            current_location = "glinstering"
        elif keuze == "2":
            print("Je gaat rechtdoor en gebruikt je zaklamp.")
            current_location = "luistert_aandachtig"
        else:
            print("Ongeldige invoer, probeer opnieuw. ")

    elif current_location == "glinstering":
        glinstering()
        keuze = input("Wat kies je? ")
        if keuze == "1":
            print("je gaat de glinstering verder onderzoeken")
            current_location = "puzzel"
        elif keuze == "2":
            current_location == "Donkere_pad"
        else:
            print("Ongeldige invoer, probeer opnieuw.")

    elif current_location == "welke_richting":
        welke_richting()
        keuze = input("Wat kies je? ")

        if keuze == "1":
            current_location = "boom"
            print("Je hebt gekozen voor het verlichte pad")
        elif keuze == "2":
            current_location = "donkere_pad"
            print("Je hebt gekozen voor het donkere pad")
        else:
            print("Ongeldige invoer probeer opnieuw")

    elif current_location == "Mysterieuze_geluiden":
        mysterieuze_geluiden()
        keuze = input("Wat kies je?")

        if keuze == "1":
            current_location = "huisje"
            print("Je gaat het pad onderzoeken")
        elif keuze == "2":
            current_location = "glinstering"
            print("Je gaat een andere kant op")
        else:
            print("Ongeldige invoer, probeer opnieuw")

    elif current_location == "Bomen_bewegen":
        bomen_bewegen()
        keuze = input("Wat ga je doen? ")
        if keuze == "1":
            print(
                "Je koos ervoor om je om te keren, omdat je het vreemd vind. Maar helaas nadat je besloot om je terug te keren werd je gevangen door een heks. Hierdoor is jouw missie beeindigd. game over."
            )
            game_over = True
        elif keuze == "2":
            current_location = "Donkere_pad"
            print("Je bent nieuwsgierig en gaat op onderzoek uit.")
        else:
            print("Ongeldige invoer, probeer opnieuw.")

    elif current_location == "puzzel":
        puzzel()
        puzzel_antwoord = input("Wat is je antwoord?")
        if puzzel_antwoord.lower() == "kaars":
            print("Goed zo! Je hebt de puzzel voltooid! ;) ")
            current_location = "huisje"
        elif puzzel_antwoord.lower() != "kaars":
            print(
                "Je hebt de puzzel niet behaald, helaas! Hierdoor heeft de fee besloten, dat je uit het bos moet. Game over."
            )
            game_over = True
        else:
            print("Ongeldige invoer, probeer opnieuw.")

    elif current_location == "huisje":
        huisje()
        keuze = input("Wat doe je?")

        if keuze == "1":
            print("je praat met de geest, hierdoor kom je erachter dat er een dorpeling in het huis zit verstopt. Dit is goed nieuws voor jou! Je gaat opzoek naar de dorpeling, na een paar minuutjes heb je hem gevonden! Gefeliciteerd, je hebt het einde behaald.")
        elif keuze == "2":
            print("Je had de geest niet moeten negeren, hij heeft je vermoord. Game Over.")
            game_over = True
        else:
            print("Ongeldige invoer, probeer opnieuw.")
    # win eind
    elif current_location == "luistert_aandachtig":
        luistert_aandachtig()
        keuze = input("Je hebt de volgende opties:")

        if keuze == "1":
            current_location = "Donkere_pad"
            print("Je gaat verder met het verkennen van het donkere pad")
        elif keuze == "2":
            print("Je vind het niet veilig en gaat naar het dorp")
            game_over = True
        else:
            print("Ongeldige invoer, probeer opnieuw.")

    elif current_location == "boom":
        boom()
        current_location = "begin_bos"
