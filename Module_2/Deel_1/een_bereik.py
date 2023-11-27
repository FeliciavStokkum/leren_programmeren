#Vraag de gebruiker een getal in te voeren
getal = int(input("Voer een getal in, waarvan je de tafel wilt weten. "))

for i in range(1, 11): 
    resultaat = getal * i #Hiermee wordt het getal keer de i gedaan
    print(f"{i} X {getal} = {resultaat}") #Hiermee wordt het getal geprint inclusief de berekening

