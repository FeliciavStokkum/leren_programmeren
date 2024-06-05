from functions import *

while True:
    choice = input("Wat wilt u doen? \n A) getallen optellen \n B) getallen aftrekken \n C) getallen vermenigvuldigen \n D) getallen delen \n E) getal ophogen \n F) getal verlagen \n G) getal verdubbelen \n H) getal halveren \n Kies: ").lower()
    number1 = input("Voer het eerste getal in: ")
    number2 = input("Voer het tweede getal in: ")
    if choice == "A":
        antwoord = addition(number1, number2)
    elif choice == "B":
        antwoord = subtraction(number1, number2)
    elif choice == "C":
        antwoord = multiplication(number1, number2)
    elif choice == "D": 
        antwoord = division(number1, number2)
    elif choice == "E":
        antwoord = addition(number1, number2)
    elif choice == "F":
        antwoord = subtraction(number1, number2)
    elif choice == "G":
        antwoord = multiplication(number1, number2)
    elif choice == "H":
        antwoord = division(number1, number2)
    break
    print(antwoord)