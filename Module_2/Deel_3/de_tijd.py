# Maak een programma met een while loop die de uren de van de dag print (2x12).
# Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe.

tijd_AM = 1
tijd_PM = 1

while tijd_AM < 25:
    if tijd_AM <= 12:
        print(f"{tijd_AM} AM")
    else:
        print(f"{tijd_PM} PM")
        tijd_PM += 1
    tijd_AM += 1