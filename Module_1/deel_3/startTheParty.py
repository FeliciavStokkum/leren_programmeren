gastheer = input("Wie is de gastheer? ")
gasten = int(input("Hoeveel gasten? "))
drank = True
chips = False
NAAM = "Felicia"
SLB = "Jouke"

if drank and gastheer or chips and drank and gasten or gastheer == NAAM and not SLB == gastheer and gasten >= 5 and gasten < 20:
    print('Start the Party')
else:
    print('No Party')