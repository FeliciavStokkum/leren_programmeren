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
deur_4 = False


print("---- Je bent nu in kamer 3 -----")

item_lijst = ['schild', 'zwaard', 'sleutel']

print("In deze kamer staat een goblin, hierbij kan je verschillende items kopen. ")
print(rupee)

if rupee > 2:
    selected_item = input(f"Je kan beide het {item_lijst[0]} en {item_lijst[1]} kopen, wil je ze allebei kopen? ja / nee")
    if selected_item == 'ja':
        selected_item = ['schild', 'zwaard']
    else:
        selected_item = input(f"Welk item wil je kopen? het {item_lijst[0]} of het {item_lijst[1]} of de {item_lijst[2]}? ")
else:
    selected_item = input(f"Je kan kiezen uit drie items, wat wil je kopen? {item_lijst[0]}, {item_lijst[1]}, {item_lijst[2]} of ga je niks kopen? ")
    print(selected_item)

    if selected_item == 'schild':
        selected_item += "schild"
        player_defense += 1
    elif selected_item == 'zwaard':
        selected_item += "zwaard"
        player_attack += 2
    elif selected_item == "sleutel":
        selected_item += "sleutel"
        player_key += 1

        print('Je duwt de deur open en stap een hele lange kamer binnen.')
        if selected_item != 'niks':
            print(f'In deze kamer staat een tafel met daarop een {selected_item}.')
            print(f'Je pakt het {selected_item} op en houdt het bij je.')
            deur_4 = input(print('wil je naar kamer 4?'))
            print('')
            time.sleep(1)

            if deur_4 == "ja":
                print("Je hebt gekozen voor kamer 4")
print(player_defense)
print(player_attack)
print(player_key)