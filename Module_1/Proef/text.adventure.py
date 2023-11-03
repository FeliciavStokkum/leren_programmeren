import time

#Hier heet je de gast welkom en vraag je naar de naam
print("Welkom bij Het Geheimzinnige bos")
time.sleep(2)
naam = input("Wat is je naam? ")
time.sleep(1)
print(f"Hoi {naam} laten we van start gaan!")

# #Hier wordt het verhaal en het doel getoond
verhaal = [
    "Je bevindt je in een rustig dorpje aan de rand van een mysterieus bos",
    "\nHet bos staat al eeuwenlang bekend om zijn geheimzinnige krachten en vreemde gebeurtenissen.",
    "\nWanneer een dorpeling plotseling verdwijnt, besluit je het bos te betreden om de waarheid te ontdekken.",
    "\nTerwijl je het bos verkent, kom je verschillende mysterieuze gebeurtenissen tegen en ontmoet je bewoners van het bos, zoals sprekende dieren, feeën en geesten.",
    "\nJe moet aanwijzingen verzamelen om te achterhalen wat er met de verdwenen dorpeling is gebeurd en hoe je hem kunt redden."
]

for line in verhaal:
    print(line)
    time.sleep(2)

doel = [
    "\nJouw doel is om de verdwenen dorpeling te vinden en het geheim van het bos te ontrafelen",
    "\nAfhankelijk van je keuzes en acties, kun je verschillende eindes bereiken."
    "\nSucces"
]

for line in doel:
    print(line)
    time.sleep(2)

#Vraag wat neem je mee
def wat_neem_je_mee():
    print("\nTerwijl je bij de rand van het bos staat, bedenk je wat je moet meenemen op je avontuur. Welke items of uitrusting kies je om je voor te bereiden voordat je het bos betreedt?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. een zaklamp")
    print("2. een broodtrommel en een flesje water")
    print("3. Een kompas en een kaart")
    
    keuze = input("Wat neem je mee? (1,2,3) ")

    if keuze == "1":
        donker_pad()
    elif keuze == "2":
        welke_richting()
    elif keuze == "3":
        mysterieuze_geluiden()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        wat_neem_je_mee()

wat_neem_je_mee()

#vraag het donkere pad 
def donker_pad():
    print("Wanneer je het bos binnengaat met je zaklamp, merk je meteen een donker pad op dat perkt tot in de diepte van het bos. Wat is je volgende stap?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. je neemt een andere route")
    print("2. je gaat rechtdoor en zet je zaklamp aan")
    print("3. je besluit om hier even te blijven wachten, tot je zeker weet dat het veilig is")

    keuze = input("Wat ga je doen? (1,2,3)")

    if keuze == "1":
        glinstering()
    elif keuze == "2":
        bomen_bewegen()
    elif keuze == "3":
        luistert_aandachtig()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        donker_pad()

donker_pad()

#vraag welke richting
def welke_richting():
    print("Met je broodtrommel en water, voel je je goed voorbereid voor je reis. Je komt echter al snel een kruispunt tegen in het bos. Welke richting kies je om verder te gaan?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. Pad 1 is verlicht")
    print("2. Pad 2 is donker, maar ziet er wel minder lang uit.")
    
    keuze = input("Welk pad neem je? (1,2)")

    if keuze == "1":
        einde_gewonnen()
    elif keuze == "2":
        einde_verloren()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        welke_richting()

welke_richting()

#vraag mysterieuze geluiden
def mysterieuze_geluiden():
    print("Met je kompas en kaart in de hand, voel je je zeker van je navigatievaardigheden. Terwijl je verder het bos in gaat, hoor je mysterieuze geluiden. Wat doe je om te onderzoeken wat er aan de hand is?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. je gaat het pad te onderzoeken")
    print("2. je gaat een andere kant op, je durf het niet aan.")
    print("3. je gaat je verschuilen op een veilige plek, tot de geluiden voorbij zijn.")

    keuze = input("Wat doe je? (1,2,3)")

    if keuze == "1":
        einde_gewonnen()
    elif keuze == "2":
        einde_verloren()
    elif keuze == "3":
        einde_verloren()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        mysterieuze_geluiden()

mysterieuze_geluiden()

#vraag glinstering
def glinstering():
    print("Terwijl je een andere route hebt gekozen, hierdoor zie je een vreemde glinstering in het bos")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. Je onderzoekt de glinstering nader")
    print("2. Je zoekt naar een andere route")

    keuze = input("Wat ga je doen? (1,2)")

    if keuze == "1":
        einde_gewonnen()
    elif keuze == "2":
        einde_verloren()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        glinstering()

glinstering()

#vraag bomen_bewegen
def bomen_bewegen():
    print("Je bent rechtdoor gegaan, hier merk je dat de bomen beginnen te bewegen.")
    time.sleep(2)
    print("Ook hoor je een soort geritsel")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. Je bent nieuwsgierig en gaat op onderzoek uit")
    print("2. Je keert je om, je vind het maar vreemd")

    keuze = input("Wat doe je? (1,2)")

    if keuze == "1":
        einde_gewonnen()
    elif keuze == "2":
        einde_verloren()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        bomen_bewegen()

bomen_bewegen()

#vraag luistert_aandachtig
def luistert_aandachtig():
    print("Je hebt besloten om even te wachten tot het veilig is")
    time.sleep(2)
    print("Na enkele minuten te hebben gewacht, merk je dat er niks aan de hand is")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("Je gaat verder met het verkennen van het donkere pad, aangezien het nu veilig is")
    print("Je vind het niet veilig genoeg en je gaat terug naar het dorp")

    keuze = input("Wat ga je doen? (1,2)")

    if keuze == "1":
        einde_gewonnen()
    elif keuze == "2":
        einde_verloren()
    else:
        print("Ongeldige invoer, probeer opnieuw!")
        luistert_aandachtig()

luistert_aandachtig()

def einde_gewonnen():
    print("Gefeliciteerd je hebt de dorpeling gevonden")

def einde_verloren():
    print("helaas je hebt de dorpeling niet gevonden.")