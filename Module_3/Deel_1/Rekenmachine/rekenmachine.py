from functions import *

func_checker_extra_opp = ["e", "f", "g", "h"]
func_checker = ["a", "b", "c", "d", "e", "f", "g", "h", ""]
text_intro = "Wat wilt u doen?\n"

full_som = ""
stoppen = ""
firstround = True

def get_number(invoer):
    print(invoer)
    return number()

while True:
    if firstround == False:
        stoppen = "Niets om te stoppen"
    text = (
        f"{text_intro}"
        "A) getallen optellen\n"
        "B) getallen aftrekken\n"
        "C) getallen vermenigvuldigen\n"
        "D) getallen delen\n"
        "E) getal ophogen\n"
        "F) getal verlagen\n"
        "G) getal verdubbelen\n"
        "H) getal halveren\n"
        f"{stoppen}\n"
    )
    func = input(text).lower()
    if func not in func_checker:
        print("Ongeldige invoer")
        continue
    
    if func == "":
        if firstround:
            print("U heeft nog niets ingevoerd")
            continue
        else:
            exit()

    if firstround:
        number1 = get_number("Eerste nummer")
        firstround = False

    if func not in func_checker_extra_opp:
        number2 = get_number("Tweede nummer")
        if func == "d" and number2 == 0:
            print("U kan niet delen door 0")
            continue

    if func == "a":
        antwoord = addition(number1, number2)
        operator = "+"
        operator_str = "optellen"

    elif func == "b":
        antwoord = subtraction(number1, number2)
        operator = "-"
        operator_str = "aftrekken"

    elif func == "c":
        antwoord = multiplication(number1, number2)
        operator = "*"
        operator_str = "vermenigvuldigen"

    elif func == "d":
        antwoord = division(number1, number2)
        operator = "/"
        operator_str = "delen"

    elif func == "e":
        antwoord = addition(number1, 1)
        operator = "+"
        operator_str = "ophogen"

    elif func == "f":
        antwoord = subtraction(number1, 1)
        operator = "-"
        operator_str = "verlagen"

    elif func == "g":
        antwoord = multiplication(number1, 2)
        operator = "*"
        operator_str = "verdubbelen"

    elif func == "h":
        antwoord = division(number1, 2)
        operator = "/"
        operator_str = "halveren"

    if func in func_checker_extra_opp:
        if func in ["h", "g"]:
            full_som += f"{number1} {operator} 2 = {antwoord}\n"
        else:
            full_som += f"{number1} {operator} 1 = {antwoord}\n"
    else:
        full_som += f"{number1} {operator} {number2} = {antwoord}\n"
    text_intro = f"{operator_str}\n{full_som} Wil je wat met de uitkomst?\n"
    number1 = antwoord