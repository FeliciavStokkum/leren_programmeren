from user_input import *

#vraagt de gebruiker de gewenste plek 
#valideert of een getal tussen 11 en 33 is ingevoerd
def get_position() -> str:
    position = 0
    while position < 11 or position > 33:
        position = get_integer("Kies een vakje tussen 11 en 33: ")

    return str(position)

#Het spelletje boter, kaas en eieren

rij_1 = ["U", "U", "U"]
rij_2 = ["U", "U", "U"]
rij_3 = ["U", "U", "U"]

print(rij_1)
print(rij_2)
print(rij_3)

#move speler_1 - speelt met X
move = get_position() #we krijgen "11" terug 
print(move)
print(move[0])