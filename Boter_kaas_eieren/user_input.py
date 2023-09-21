def get_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            integer_value = int(user_input)
            return integer_value
        else:
            print("Ongeldige invoer, Voer een geldig getal in: ")

#---------------------------------------------------------------------------

def get_float(prompt):
    while True:
        user_input = input(prompt)

        try:
            float_value = float(user_input)
            return float_value
        except ValueError:
            print("Ongeldige invoer. Voer een gelid float getal in!")

# #----------------------------------------------------------------------------

def getString(prompt):
    user_input = input(prompt)
    return user_input
    

#----------------------------------------------------------------------------
 
def get_letter(prompt):
    while True:
        user_input = input(prompt)
        try: 
            if len(user_input) == 1:
                letter = user_input.upper()
                if "A" <= letter <= "Z":
                    return letter
        except:
            pass


        print("Ongeldige invoer. Voer precies een letter van het alfabet in.")

#-------------------------------------------------------------------------------