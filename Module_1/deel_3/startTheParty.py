gastheer = input("Wie is de gastheer? ")
gasten = int(input("Hoeveel gasten komen er? "))
drank = False
chips = True
NAAM = "Felicia"
SLB = "Jouke"

if chips and drank or gasten and chips and drank or gastheer and drank or gastheer and gasten and chips and drank and gastheer == NAAM or gastheer == SLB or gasten >= 4 and gasten <20:
    print('Start the Party')
else:
    print('No Party')