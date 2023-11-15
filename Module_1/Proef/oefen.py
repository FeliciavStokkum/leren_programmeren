curr_loc = "start"
game_over = False

while not game_over:
    if curr_loc == "start":
        print('start verhaal')
        curr_loc = "bos"

    elif curr_loc == "bos":
        print('bos verhaal')
        keuze = input("Wel of niet heks?")

        if keuze == "wel":
            curr_loc = "heks"
        else:
            keuze_2 = input("Ren je weg?")
            if keuze_2 == "ja":
                curr_loc = "wolf"
            else:
                curr_loc = "blijven"

    elif curr_loc == "heks":
        print("De heks heeft je te pakken")
        game_over = True

    elif curr_loc == "wolf":
        print("De wolf vreet je op")
        game_over = True

    elif curr_loc == "blijven":
        print("Je woont in het bos en blijft leven! Hoera")
        game_over = True  

print("Einde pgm")
