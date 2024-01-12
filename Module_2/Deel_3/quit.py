#Stel de vraag "?" aan de gebruiker
#Zolang er geen quit wordt geantwoord stel je de vraag opnieuw
#Print het aantal keer dat de vraag is gesteld

woord = " "
teller = 0

while woord != "quit":
    woord = input("?")
    teller += 1

print(f"De vraag is {teller} keer gesteld.")