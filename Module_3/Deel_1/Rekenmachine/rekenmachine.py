from functions import addition, subtraction, multiplication, division

while True:
    choice = input("Wat wilt u doen? \n A) getallen optellen \n B) getallen aftrekken \n C) getallen vermenigvuldigen \n D) getallen delen \n E) getal ophogen \n F) getal verlagen \n G) getal verdubbelen \n H) getal halveren \n Kies: ")
    number1 = input("Voer het eerste getal in: ")
    number2 = input("Voer het tweede getal in: ")
    if choice == "A".lower():
        addition(number1, number2)
        print(addition(sum))
    elif choice == "B".lower():
        break
    elif choice == "C".lower():
        break
    elif choice == "D".lower():
        break
    elif choice == "E".lower():
        break
    elif choice == "F".lower():
        break
    elif choice == "G".lower():
        break
    elif choice == "H".lower():
        break