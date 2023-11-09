import time

from text_adventure_functies import *

#Hier heet je de gast welkom en vraag je naar de naam
# print("Welkom bij Het Geheimzinnige bos")
# time.sleep(2)
# naam = input("Wat is je naam? ")
# time.sleep(1)
# print(f"Hoi {naam} laten we van start gaan!")

# # #Hier wordt het verhaal en het doel getoond
# verhaal = [
#     "Je bevindt je in een rustig dorpje aan de rand van een mysterieus bos",
#     "\nHet bos staat al eeuwenlang bekend om zijn geheimzinnige krachten en vreemde gebeurtenissen.",
#     "\nWanneer een dorpeling plotseling verdwijnt, besluit je het bos te betreden om de waarheid te ontdekken.",
#     "\nTerwijl je het bos verkent, kom je verschillende mysterieuze gebeurtenissen tegen en ontmoet je bewoners van het bos, zoals sprekende dieren, feeën en geesten.",
#     "\nJe moet aanwijzingen verzamelen om te achterhalen wat er met de verdwenen dorpeling is gebeurd en hoe je hem kunt redden."
# ]

# for line in verhaal:
#     print(line)
#     time.sleep(2)

# doel = [
#     "\nJouw doel is om de verdwenen dorpeling te vinden en het geheim van het bos te ontrafelen",
#     "\nAfhankelijk van je keuzes en acties, kun je verschillende eindes bereiken."
#     "\nSucces"
# ]

# for line in doel:
#     print(line)
#     time.sleep(2)


wat_neem_je_mee()
    
keuze = input("Wat neem je mee? (1,2,3) ")

if keuze == "1":
    welk_pad
    answer = input("Welk pad? (1/2)")

    if answer == "1":
        donker_pad()
        answer = input("welk route")
        if answer == '!':
            welke_richting
    elif answer != "1":
        lichte_pad()

elif keuze == "2":
    welke_richting()
elif keuze == "3":
    mysterieuze_geluiden()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    wat_neem_je_mee()

donker_pad()

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

welke_richting()

keuze = input("Welk pad neem je? (1,2)")

if keuze == "1":
    einde_gewonnen()
elif keuze == "2":
    einde_verloren()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    welke_richting()

mysterieuze_geluiden()

keuze = input("Wat doe je? (1,2,3)")

if keuze == "1":
    dorpeling()
elif keuze == "2":
    einde_verloren()
elif keuze == "3":
    einde_verloren()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    mysterieuze_geluiden()

glinstering()

keuze = input("Wat ga je doen? (1,2)")

if keuze == "1":
    einde_gewonnen()
elif keuze == "2":
    einde_verloren()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    glinstering()

bomen_bewegen()

keuze = input("Wat doe je? (1,2)")

if keuze == "1":
    einde_gewonnen()
elif keuze == "2":
    einde_verloren()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    bomen_bewegen()

luistert_aandachtig()

keuze = input("Wat ga je doen? (1,2)")

if keuze == "1":
    einde_gewonnen()
elif keuze == "2":
    einde_verloren()
else:
    print("Ongeldige invoer, probeer opnieuw!")
    luistert_aandachtig()


dorpeling()