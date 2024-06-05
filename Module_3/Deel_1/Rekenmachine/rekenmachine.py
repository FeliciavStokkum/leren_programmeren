from functions import *

while True:
    while True:
        choice = input("Wat wilt u doen? \n A) getallen optellen \n B) getallen aftrekken \n C) getallen vermenigvuldigen \n D) getallen delen \n E) getal ophogen \n F) getal verlagen \n G) getal verdubbelen \n H) getal halveren \n Kies: ").lower()
        
        if choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            number1 = int(input("Wat is je eerste getal: "))
            break 
        else:
            print("Dat is geen keuze, probeer opnieuw")

    if choice == "a":
        number2 = int(input(f"Welk getal wil je bij {number1} optellen: "))
        antwoord = addition(number1, number2)
    elif choice == "b":
        number2 = int(input(f"Welk getal wil je van {number1} aftrekken: "))
        antwoord = subtraction(number1, number2)
    elif choice == "c":
        number2 = int(input(f"Welk getal wil je met {number1} vermenigvuldigen: "))
        antwoord = multiplication(number1, number2)
    elif choice == "d":
        number2 = int(input(f"Met welk getal wil je {number1} delen: "))
        antwoord = division(number1, number2)
    elif choice == "e":
        antwoord = addition(number1, 1)
    elif choice == "f":
        antwoord = subtraction(number1, 1)
    elif choice == "g":
        antwoord = multiplication(number1, 2)
    elif choice == "h":
        antwoord = division(number1, 2)
    
    print(f"Het antwoord is: {antwoord}")