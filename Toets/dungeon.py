import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_key = 0
rupee = 0

deur_1 = False
kamer_3 = False
keuze_kamer_3 = False
keuze_richting = False

# === [kamer 1] === #
print("---- Je bent nu in kamer 1 ----")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [Kamer 7] === #
print("---- Je bent nu in kamer 7 ----")

print("De wizard heeft deze kamer betoverd, er is nu een kans van 1 op 10 dat je geen rupee krijgt.")

kans_geen_rupee = random.randint(1, 10)

if kans_geen_rupee == 1:
    rupee = 0
    print("Helaas krijg je geen rupee.")
else:
    print("Je krijgt wel een rupee van de wizard, gefeliciteerd.")
    rupee += 1
    print(f"Je hebt nu {rupee} rupees")
    print("")
    time.sleep(1)

    print("Wil je rechtdoor of naar rechts?")
    keuze_richting = input("Type: rechtdoor of rechts ")

    if keuze_richting == "rechtdoor":
        print("Je hebt gekozen voor: rechtdoor")
    elif keuze_richting == "rechts":
        print("je hebt gekozen voor rechts")

# === [kamer 2] === #
if keuze_richting == "rechtdoor":
        print("---- Je bent nu in kamer 2 ----")
        getal_1 = random.randint(10, 25)
        getal_2 = random.randint(-5, 75)
        antwoord_som = getal_1 + getal_2

        print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
        print('Het standbeeld heeft een rupee vast.')
        print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
        print(f'Daarboven zie je een som staan {getal_1} + {getal_2}?')
        antwoord = int(input('Wat toets je in?'))

        if antwoord == antwoord_som:
            print('Het standbeeld laat de rupee vallen en je pakt het op')
            rupee += 1
            print(f"Je hebt nu {rupee} rupees. ")
        else:
            print('Er gebeurt niets....')

            print('Je ziet een deur achter het standbeeld.')
            print('')
            time.sleep(1)

        print("Je ziet twee deuren, kies je voor kamer 1 of voor kamer 2? ")
        antwoord_deur = input("Type 1 of 2: ")

        if antwoord_deur == "1":
            deur_1 = True
        elif antwoord_deur == "2":
            deur_1 = False

        
# === [kamer 6] === #
if deur_1:
    print("---- Je bent nu in kamer 6 ----")
    print("Je komt kamer 6 binnen, hier is een zombie. ")

    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2

    zombie_hit_damage = max(zombie_attack - player_defense, 0)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

        player_hit_damage = max(player_attack - zombie_defense, 0)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        player_health -= player_attack_amount * zombie_hit_damage

    if player_health > 0:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
        kamer_3 = input("Wil je door naar kamer 3? ja/nee")
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
    print('')
    time.sleep(1)

    if kamer_3 == "ja":
        print("Je hebt gekozen om naar kamer 3 te gaan. ")

# === [kamer 8] === #
if keuze_richting == "rechts" or deur_1 == False:
    print("---- Je bent nu in kamer 8 ----")
    print("Als je de kamer binnen loopt zie je een gokmachine. Wil je de gokmachine gebruiken? ")

    gokken = input("Wil je de gokmachine gebruiken? ja / nee ")

    while gokken != 'nee':
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        totaal = dobbelsteen1 + dobbelsteen2

        if totaal > 7:
            print(f'Gefeliciteerd! Je hebt meer dan 7 gegooid, dus je verdubbelt het aantal ruppees.')
            rupee *= 2
            print(f'Je hebt nu {rupee} rupees.')
        elif totaal < 7:
            print('Helaas, je hebt minder dan 7 gegooid. Je verliest 1 health.')
            player_health -= 1
            print(f'Je health is nu {player_health}.')

        else:
            print('Oei, het totaal is 7. Je verdubbelt het aantal rupees die je hebt, maar verliest ook 1 health.')
            rupee *= 2
            player_health -= 1
            print(f'Je hebt nu {rupee} rupees en je health is {player_health}.')
                                    
            if player_health == 0:
                print("Helaas, je hebt verloren! Volgende keer beter")
                exit()
            gokken = input("Wil je de gokmachine nog een keer gebruiken? ja / nee ")
                
    if gokken == "nee":
        keuze_kamer_3 = input("Wil je door naar kamer 3? ja/ nee ")
        if keuze_kamer_3 == "ja":
            print("Je hebt gekozen voor kamer 3")

# === [kamer 9] === #
    if kamer_3 == "nee" or keuze_kamer_3 == "nee":
        print("---- Je bent nu in kamer 9 ----")
                                
        random_betovering = random.choice(["player_defense", "player_health"])
                                
        if random_betovering == "player_defense":
            player_defense += 1
            print("Je hebt 1 defence erbij gekregen.")
            print(f"Je defence is nu {player_defense}")
        else:
            player_health += 2
            print("Je hebt 2 health erbij gekregen.")
            print(f"Je health is nu {player_health}")

# === [kamer 3] === #
if kamer_3 == "ja" or keuze_kamer_3 == "ja":
    print("---- Je bent nu in kamer 3 -----")

    item_lijst = ['schild', 'zwaard', 'sleutel']

    print("In deze kamer staat een goblin, hierbij kan je verschillende items kopen. ")

    if rupee > 2:
        selected_item = input(f"Je kan beide het {item_lijst[0]} en {item_lijst[1]} kopen, wil je ze allebei kopen? ja / nee")
        if selected_item == 'ja':
                selected_item = ['schild', 'zwaard']
        else:
            selected_item = input(f"Welk item wil je kopen? het {item_lijst[0]} of het {item_lijst[1]} of de {item_lijst[2]}? ")
    else:
        selected_item = input(f"Je kan kiezen uit drie items, wat wil je kopen? {item_lijst[0]}, {item_lijst[1]}, {item_lijst[2]} of ga je niks kopen? ")

        if selected_item == 'schild':
                player_defense += 1
        elif selected_item == 'zwaard':
                player_attack += 2
        elif selected_item == "sleutel":
            player_key += 1

            print('Je duwt de deur open en stap een hele lange kamer binnen.')
            if selected_item != 'niks':
                print(f'In deze kamer staat een tafel met daarop een {selected_item}.')
                print(f'Je pakt het {selected_item} op en houdt het bij je.')
                print('Op naar de volgende deur.')
                print('')
                time.sleep(1) 

# === [kamer 4] === #
print("---- Je bent nu in kamer 4 ----")
trol_attack = 2
trol_defense = 0
trol_health = 3
print('Je loopt verder in de kamer, hier kom je een trol tegen.')

trol_hit_damage = max(trol_attack - player_defense, 0)
if trol_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de trol, hij kan je geen schade doen.')
else:
    trol_attack_amount = math.ceil(player_health / trol_hit_damage)
                    
    player_hit_damage = max(player_attack - trol_defense, 0)
    player_attack_amount = math.ceil(trol_health / player_hit_damage)

    player_health -= player_attack_amount * trol_hit_damage

    if player_health > 0:
        print(f'In {player_attack_amount} rondes versla je de trol.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de trol te sterk voor je.')
        print('Game over.')
        exit()
    print('')
    time.sleep(1)

# === [kamer 10] === #
print("---- Je bent nu in kamer 10 ----")
print("Terwijl je de kamer in loopt zie je de dungeon boss.")
dungeon_boss_attack = 3
dungeon_boss_defence = 1
dungeon_boss_health = 5

dungeon_boss_damage = (dungeon_boss_attack - player_defense)
if dungeon_boss_damage <= 0:
    print('Jij hebt een te goede verdediging voor de dungeon boss, hij kan je geen schade doen.')
else:
    dungeon_boss_attack = math.ceil(player_health / dungeon_boss_damage)
                        
    player_hit_damage = max(player_attack - dungeon_boss_defence, 0)
    player_attack_amount = math.ceil(dungeon_boss_health / player_hit_damage)

    player_health -= player_attack_amount * dungeon_boss_damage

    if player_health >= 0:
        print(f'In {player_attack_amount} rondes versla je de dungeon boss.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de dungeon boss te sterk voor je.')
        print('Game over.')
        exit()
    print('')
    time.sleep(1)

# === [kamer 5] === #
print("---- Je bent nu in kamer 5 ----")
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
time.sleep(1)

if player_key == 1:
    print("Door de rekensom heb je een sleutel, hiermee kan je de schatkist openen. Je hebt het spel gewonnen.")
else:
    print("Door de rekensom heb je geen sleutel, je kan helaas de kist niet openen. Je verliest het spel.")