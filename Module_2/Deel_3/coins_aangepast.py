toPay = int(float(input('Amount to pay: ')) * 100) 
paid = int(float(input('Paid amount: ')) * 100)
change = paid - toPay 

muntstukken_teruggegeven = {}

if change > 0:
    coinValue = 500
  
    while change > 0 and coinValue > 0:
        nrCoins = change // coinValue 

        if nrCoins > 0:
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' )
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) 
            change -= nrCoinsReturned * coinValue 

            if coinValue in muntstukken_teruggegeven:
                muntstukken_teruggegeven[coinValue] += nrCoinsReturned
            else:
                muntstukken_teruggegeven[coinValue] = nrCoinsReturned

        if coinValue == 500:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 100
        elif coinValue == 100:
            coinValue = 50
        elif coinValue == 50:
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

if change > 0: 
    print('Change not returned: ', str(change) + ' cents')
else:
    print('done')

print('Overzicht van teruggegeven muntstukken:')
if muntstukken_teruggegeven: 
    for muntstuk, aantal in muntstukken_teruggegeven.items():
        print(f'{aantal} muntstuk(ken) van {muntstuk} cent(en)')
else:
    print('Geen munten teruggegeven.')