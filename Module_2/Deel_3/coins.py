# name of student:  Felicia van Stokkum
# number of student: 99057214
# purpose of program: Wisselgeld terug geven met de juiste hoeveelheid munten van een bepaalde soort 
# function of program: wisselgeld berekenen
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #hier wordt er gevraagd om het bedrag wat de klant moet betalen, hier worden centen van gemaakt door * 100
paid = int(float(input('Paid amount: ')) * 100) #hier wordt er gevraagd naar de hoeveelheid dat er betaald is ook dit wordt omgezet in centen
change = paid - toPay #hier wordt het overige geld (wisselgeld) berekend door het bedrag dat er betaald is min het bedrag gaat wat er moet betaald worden

if change > 0: #als het wisselgeld groter dan 0 is, word het proces gestart waarbij er wisselgeld teruggegeven moet worden, deze begin bij 50
  coinValue = 50 #hier begint het wisselgeld bij 50
  
  while change > 0 and coinValue > 0: #zolang het wisselgeld en de coinvalue groter zijn als 0
    nrCoins = change // coinValue #hier wordt berekend hoeveel wisselgeld er teruggegeven moet worden, door middel van een floor division (deze deelt het eerste argument door het tweede en rondt het resultaat af naar het dichtsbijzijnde gehele getal.)

    if nrCoins > 0: #hier wordt gekeken of het aantal wisselgeld groter is als 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hier word eerst geprint hoeveel er maximaal teruggegeven kan worden, daarna wordt de grootte van de cent getoond
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hier wordt er gevraagd hoeveel cent je terug hebt gekregen
      change -= nrCoinsReturned * coinValue #hier wordt de change opnieuw berekend, daarna wordt het berekend naar centen

# comment on code below: hier wordt de coinValue aangepast naar de huidige waarde, dus als de CoinValue gelijk is aan 50 wordt dat 20. 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
      
    else:
      coinValue = 0

if change > 0: #als het wisselgeld hoger is als 0, dan wordt er aangegeven hoeveel wisselgeld er niet is terug gegeven. En anders print hij done. 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')