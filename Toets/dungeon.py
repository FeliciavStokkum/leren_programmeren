import time, math, random
from random import choice

player_attack = 1
player_defense = 0
player_health = 3

player_key = 0
rupee = 0

# === [kamer 1] === #
print("")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [Kamer 7] === #
print("Je krijgt een rupee, hier kan je verder in het spel dingen van halen. ")
print("Dit kan alleen bij een verkooppunt. ")
rupee += 1
print(f"Je hebt nu {rupee} rupee")
print("")
time.sleep(1)

# === [kamer 2] === #
getal_1 = random.randint(10, 25)
getal_2 = random.randint(-5, 75)
antwoord_som = getal_1 + getal_2

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
print(f'Daarboven zie je een som staan {getal_1} + {getal_2}?')
antwoord = int(input('Wat toets je in?'))

if antwoord == antwoord_som:
    print('Het standbeeld laat de sleutel vallen en je pakt het op')
    player_key += 1
else:
    print('Er gebeurt niets....')

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(1)

print("Je ziet twee deuren, kies je voor kamer 1 of voor kamer 2? ")
deur = int(input("Type 1 of 2: "))

if deur == 1:
    deur_3 = True
elif deur == 2:
    deur_3 = False

# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2

if deur_3 == True:
    print("Je komt kamer 6 binnen, hier is een zombie. ")

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        player_health = player_attack_amount * zombie_hit_damage
        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
        print('')
        time.sleep(1)

# === [kamer 3] === #
if deur_3 == False:
    print("Je bent nu in kamer drie.")

    print("Goblin: hoi! Ik ben een Goblin, ik verkoop verschillende dingen, voor nu kan je kiezen voor: een schild of een zwaard.")
    print("Per item kost dit 1 rupee, kies verstandig!")

    item = input("Wat kies je? zwaard/schild")

    if item == "schild":
        player_defense += 1
    elif item == "zwaard":
        player_attack += 2

    print('Je duwt de deur open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

# === [kamer 4] === #
trol_attack = 2
trol_defense = 0
trol_health = 3
print('Je loopt verder in de kamer, hier kom je een trol tegen.')

trol_hit_damage = (trol_attack - player_defense)
if trol_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de trol, hij kan je geen schade doen.')
else:
    trol_attack_amount = math.ceil(player_health / trol_hit_damage)
    
    trol_hit_damage = (player_attack - trol_defense)
    player_attack_amount = math.ceil(trol_health / trol_hit_damage)

    player_health = player_attack_amount * trol_hit_damage
    if player_attack_amount < trol_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de trol te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
time.sleep(1)

if player_key == 1:
    print("Door de rekensom heb je een sleutel, hiermee kan je de schatkist openen. Je hebt het spel gewonnen.")
else:
    print("Door de rekensom heb je geen sleutel, je kan helaas de kist niet openen. je verliest het spel.")