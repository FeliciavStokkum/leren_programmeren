import time

#Hier heet je de gast welkom en vraag je naar de naam
print("Welkom bij Het Geheimzinnige bos")
time.sleep(2)
naam = input("Wat is je naam? ")
time.sleep(1)
print(f"Hoi {naam} laten we van start gaan!")

#Hier wordt het verhaal en het doel getoond
verhaal = [
    "Je bevindt je in een rustig dorpje aan de rand van een mysterieus bos",
    "\nHet bos staat al eeuwenlang bekend om zijn geheimzinnige krachten en vreemde gebeurtenissen.",
    "\nWanneer een dorpeling plotseling verdwijnt, besluit je het bos te betreden om de waarheid te ontdekken.",
    "\nTerwijl je het bos verkent, kom je verschillende mysterieuze gebeurtenissen tegen en ontmoet je bewoners van het bos, zoals sprekende dieren, feeën en geesten.",
    "\nJe moet aanwijzingen verzamelen om te achterhalen wat er met de verdwenen dorpeling is gebeurd en hoe je hem kunt redden."
]

for line in verhaal:
    print(line)
    time.sleep(4)

doel = [
    "\nJouw doel is om de verdwenen dorpeling te vinden en het geheim van het bos te ontrafelen",
    "\nAfhankelijk van je keuzes en acties, kun je verschillende eindes bereiken."
]

for line in doel:
    print(line)
    time.sleep(4)

#Keuze 1
def wat_neem_je_mee():
    print("Terwijl je bij de rand van het bos staat, bedenk je wat je moet meenemen op je avontuur. Welke items of uitrusting kies je om je voor te bereiden voordat je het bos betreedt?")
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
    elif keuze == "2":
    elif keuze == "3":

def welke_richting():
    print("Met je broodtrommel en water, voel je je goed voorbereid voor je reis. Je komt echter al snel een kruispunt tegen in het bos. Welke richting kies je om verder te gaan?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. Pad 1 is verlicht")
    print("2. Pad 2 is donker, maar ziet er wel minder lang uit.")
    
    keuze = input("Welk pad neem je? (1,2)")

    if keuze == "1":
    elif keuze == "2":

def mysterieuze_geluiden():
    print("Met je kompas en kaart in de hand, voel je je zeker van je navigatievaardigheden. Terwijl je verder het bos in gaat, hoor je mysterieuze geluiden. Wat doe je om te onderzoeken wat er aan de hand is?")
    time.sleep(2)
    print("Je hebt de volgende opties:")
    time.sleep(2)
    print("1. je gaat het pad te onderzoeken")
    print("2. je gaat een andere kant op, je durf het niet aan.")
    print("3. je gaat je verschuilen op een veilige plek, tot de geluiden voorbij zijn.")

    keuze = input("Wat doe je? (1,2,3)")

    if keuze == "1"
    elif keuze == "2":
    elif keuze == "3":

