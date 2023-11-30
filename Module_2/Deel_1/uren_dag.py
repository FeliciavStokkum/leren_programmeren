# Maak een programma met één (1) for loop die de hele uren van de dag print (2x12).

# (Geneste for loops mogen wel, geen 2 aparte for loops)

# Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe

for ochtend in range(1, 13):
    print(f"{ochtend} AM")
    if ochtend == 12:
        for middag in range(1, 13):
            print(f"{middag} PM")
