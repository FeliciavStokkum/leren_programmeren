#Een functie die twee getallen binnenkrijgt en vervolgens de kleinste van de 2 terug geeft 
def get_smallest(getal1: int, getal2: int) -> str: #Een functie kun je 1 of meer parameters meegeven!
    kleinste = 0
    if getal1 > getal2:
        kleinste = getal2
    else:
        kleinste = getal1
    return "Het kleinste getal is:" + str(kleinste) #Geeft terug: het kleinste getal is: x

#Eventuele variabele/ constantes

#Programmacode

print(get_smallest(2,4)) #argumenten
print(get_smallest(6,5)) #argumenten
print(get_smallest(15,15)) #argumenten