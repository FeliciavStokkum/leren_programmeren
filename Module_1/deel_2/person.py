# Maak een programma person.py dat de gebruiker om zijn naam, adres,
# postcode en woonplaats vraagt met duidelijke prompts.

# Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal:


naam = input("Vul hier je naam in: ")
adres = input("Vul hier je adres in: ")
postcode = input("Vul hier je postcode in: ")
woonplaats = input("Vul hier je woonplaats in: ")

print("-----------------------------------------------------------------")
print(f"| naam       : {naam}")  
print(f"| adres      : {adres}")  
print(f"| postcode   : {postcode}")  
print(f"| woonplaats : {woonplaats}")  
print("-----------------------------------------------------------------")